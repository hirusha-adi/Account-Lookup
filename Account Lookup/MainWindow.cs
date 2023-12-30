using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Linq;
using System.Net.Http;
using System.Diagnostics;
using Newtonsoft.Json.Linq;

namespace Account_Lookup
{
    public partial class MainWindow : Form
    {

        private List<Dictionary<string, string>> foundAccounts = new List<Dictionary<string, string>>();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void searchToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void clearToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void guideToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void howItWorksToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void licenseToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void creditsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void contributeToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button_search_Click(object sender, EventArgs e)
        {
            string username = field_username.Text;
            searchAndAdd(username);
        }

        private async void searchAndAdd(string username)
        {
            foundAccounts.Clear();
            dataGridView1.Rows.Clear();

            string jsonData = File.ReadAllText("wmn-data.json");
            dynamic data = JsonConvert.DeserializeObject(jsonData);

            using (HttpClient client = new HttpClient())
            {
                foreach (var site in data.sites)
                {
                    bool result = await CheckUsernameOnSite(client, site, username);
                    if (result)
                    {
                        AddToDataGridView(site);
                    }
                }
            }

            if (foundAccounts.Count == 0)
            {
                MessageBox.Show($"Username {username} not found on any site.");
            }
        }

        private async Task<bool> CheckUsernameOnSite(HttpClient client, dynamic site, string username)
        {
            string uri = site.uri_check.ToString().Replace("{account}", username);
            try
            {
                HttpResponseMessage response;

                if (site.method == "POST")
                {
                    var content = new StringContent(site.post_body.ToString(), System.Text.Encoding.UTF8, "application/json");
                    response = await client.PostAsync(uri, content);
                }
                else
                {
                    response = await client.GetAsync(uri);
                }

                response.EnsureSuccessStatusCode();

                HttpStatusCode statusCode = response.StatusCode;
                int expectedStatusCode = Convert.ToInt32(site.e_code);

                if (statusCode == (HttpStatusCode)expectedStatusCode &&
                    response.Content.ReadAsStringAsync().Result.Contains(site.e_string.ToString()))
                {
                    return true;
                }
                else if (statusCode == (HttpStatusCode)Convert.ToInt32(site.m_code) &&
                         response.Content.ReadAsStringAsync().Result.Contains(site.m_string.ToString()))
                {
                    return false;
                }
            }
            catch (HttpRequestException ex)
            {
                Console.WriteLine($"Error occurred for {site.name} - {ex.Message}");
            }

            return false;
        }

        private void AddToDataGridView(dynamic site)
        {
            int id = foundAccounts.Count + 1;
            string name = site.name.ToString();
            string status = "Claimed";

            Dictionary<string, string> accountInfo = new Dictionary<string, string>
            {
                { "id", id.ToString() },
                { "name", name },
                { "status", status }
            };

            foundAccounts.Add(accountInfo);

            dataGridView1.Rows.Add(id, name, status);
        }
        private string ExtractMainUrl(string inputUrl)
        {
            try
            {
                Uri parsedUrl = new Uri(inputUrl);
                return $"{parsedUrl.Scheme}://{parsedUrl.Host}/";
            }
            catch
            {
                return inputUrl;
            }
        }



    }
}
