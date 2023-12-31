import os, sys
import requests
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from colorama import init, Fore
from tabulate import tabulate

init(autoreset=True)

found_accounts = []

def extract_main_url(input_url):
    try:
        try:
            parsed_url = urlparse(input_url)
            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        except Exception as e:
            print(f"{Fore.RED}Error 005: Unable to parse URL: {input_url}. Exception: {e}")
        return main_url
    except:
        return input_url 

def check_username_on_site(site, username, session):
    uri = site.get("uri_check")
    method = site.get("method", "GET")
    payload = site.get("post_body", {})
    headers = site.get("headers", {})

    try:
        if method == "GET":
            final_url = uri.format(account=username)
            try:
                response = session.get(final_url, headers=headers, timeout=10)
            except requests.exceptions.ConnectionError as e:
                print(f"{Fore.RED}Error 003: Connection error. Unable to GET: {final_url}. Exception: {e}")
        elif method == "POST":
            final_url = uri
            try:
                response = session.post(final_url, data=payload, headers=headers, timeout=10)
            except requests.exceptions.ConnectionError as e:
                print(f"{Fore.RED}Error 004: Connection error. Unable to POST: {final_url}. Exception: {e}")

        response.raise_for_status()

        if response.status_code == site["e_code"] and site["e_string"] in response.text:
            account_info = {
                "id": len(found_accounts) + 1,
                "username": username,
                "name": site.get("name"),
                "url_main": extract_main_url(final_url),
                "url_user": final_url,
                "exists": "Claimed",
                "http_status": response.status_code,
                "response_time_s": f"{response.elapsed.total_seconds():.3f}",
            }
            print(f"{Fore.GREEN}[+] {username} found in {account_info['name']}, at: {account_info['url_user']}")
            found_accounts.append(account_info)
            return True
        elif response.status_code == site["m_code"] and site["m_string"] in response.text:
            return False

    except requests.exceptions.RequestException:
        print(f"{Fore.LIGHTBLACK_EX}[-] {username} not found in {site['name']}")

    return False

def check_username(username):
    with open('wmn-data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    with ThreadPoolExecutor() as executor, requests.Session() as session:
        futures = [executor.submit(check_username_on_site, site, username, session) for site in data["sites"]]
        results = [future.result() for future in futures]

    if not any(results):
        print(f"{Fore.YELLOW}Username {username} not found on any site.")
    else:
        print("\nFound Accounts:")
        for account_info in found_accounts:
            print(account_info)
    
    return found_accounts

def save_to_json():
    with open('found_accounts.json', 'w', encoding='utf-8') as outfile:
        json.dump(found_accounts, outfile, indent=2)
    print(f"{Fore.GREEN}Data saved to found_accounts.json")

def print_logo():
    logo = """
╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐  ╦  ┌─┐┌─┐┬┌─┬ ┬┌─┐
╠═╣│  │  │ ││ ││││ │   ║  │ ││ │├┴┐│ │├─┘
╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴   ╩═╝└─┘└─┘┴ ┴└─┘┴  
    """
    print(f"{Fore.CYAN}{logo}\n")

def check_json_file_download():
    if not os.path.isfile('wmn-data.json'):
        try:
            response  = requests.get("https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json")
            if response.status_code == 200:
                with open('wmn-data.json', 'wb') as f:
                    f.write(response.content)
            else:
                print(f"{Fore.RED}Error 002: Unable to download 'wmn-data.json'. Please load the data manually. Save https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json to the current working directory.")
                sys.exit()
        except requests.exceptions.ConnectionError as e:
            print(f"{Fore.RED}Error 001: Connection error. Unable to download 'wmn-data.json'. Exception: {e}")
            sys.exit()

def tabulated_accounts():
    print("\nTabulated View:")
    headers = ["ID", "Username", "Name", "URL Main", "URL User", "Exists", "HTTP Status", "Response Time (s)"]
    table_data = [[info.get(header.lower()) for header in headers] for info in found_accounts]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check if a username exists on various sites.")
    parser.add_argument("--username", help="Username to check")
    parser.add_argument("--save", action="store_true", help="Save results to a JSON file")
    
    args = parser.parse_args()

    check_json_file_download()
    
    if args.username:
        tmp = check_username(args.username)
    else:
        print_logo()
        username_to_check = input("[?] Enter the username to check: ")
        tmp = check_username(username_to_check)

    if args.save:
        save_to_json()
    else:
        save_prompt = input(f"[?] Do you want to save {len(tmp)} results? (yes/no): ").lower()
        if save_prompt == "yes":
            save_to_json()
        else:
            print("Data not saved.")

    if found_accounts:
        try:
            tabulated_accounts()
        except Exception as e:
            print(f"{Fore.RED}[-] Error tabulating data. Exception: {e}")
            