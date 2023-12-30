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

        private readonly List<FoundAccount> foundAccounts = new List<FoundAccount>();
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
            dataGridView1.Rows.Clear();
            foundAccounts.Clear();

            using (HttpClient client = new HttpClient())
            {
                await Task.WhenAll(getResults(client, username));
            }

            if (foundAccounts.Count == 0)
            {
                MessageBox.Show($"Username {username} not found on any site.");
            }
            else
            {
                foreach (var accountInfo in foundAccounts)
                {
                    dataGridView1.Rows.Add(accountInfo.Id, accountInfo.Name, accountInfo.Exists);
                }
            }
        }

        private async Task getResults(HttpClient client, string username)
        {
            try
            {
                string jsonContent = File.ReadAllText("wmn-data.json", Encoding.UTF8);

                var data = JObject.Parse(jsonContent);
                var sites = data["sites"];

                var tasks = new List<Task>();

                foreach (var site in sites)
                {
                    tasks.Add(checkUsernameOnSite(client, site, username));
                }

                await Task.WhenAll(tasks);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error occurred - {ex.Message}");
            }
        }

        private async Task checkUsernameOnSite(HttpClient client, JToken site, string username)
        {
            var uri = site.Value<string>("uri_check");
            var method = site.Value<string>("method") ?? "GET";
            var payload = site.Value<JObject>("post_body");
            var headers = site.Value<JObject>("headers");

            try
            {
                Stopwatch stopwatch = new Stopwatch();
                stopwatch.Start();

                HttpResponseMessage response;

                if (method == "GET")
                {
                    var finalUrl = string.Format(uri, username);
                    response = await client.GetAsync(finalUrl);
                }
                else if (method == "POST")
                {
                    var finalUrl = uri;
                    response = await client.PostAsync(finalUrl, new StringContent(payload.ToString()));
                }
                else
                {
                    throw new NotSupportedException("Unsupported HTTP method.");
                }

                stopwatch.Stop();

                response.EnsureSuccessStatusCode();

                var responseContent = await response.Content.ReadAsStringAsync();

                if ((int)response.StatusCode == site.Value<int>("e_code") && responseContent.Contains(site.Value<string>("e_string")))
                {
                    var accountInfo = new FoundAccount
                    {
                        Id = foundAccounts.Count + 1,
                        Username = username,
                        Name = site.Value<string>("name"),
                        UrlMain = extractMainUrl(response.RequestMessage.RequestUri),
                        UrlUser = response.RequestMessage.RequestUri.ToString(),
                        Exists = "Claimed",
                        HttpStatus = response.StatusCode,
                        ResponseTimeS = stopwatch.Elapsed.TotalSeconds.ToString("F3"),
                    };
                    foundAccounts.Add(accountInfo);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error occurred for {site["name"]} - {ex.Message}");
            }
        }

        private string extractMainUrl(Uri inputUri)
        {
            return $"{inputUri.Scheme}://{inputUri.Host}/";
        }


        public class FoundAccount
        {
            public int Id { get; set; }
            public string Username { get; set; }
            public string Name { get; set; }
            public string UrlMain { get; set; }
            public string UrlUser { get; set; }
            public string Exists { get; set; }
            public HttpStatusCode HttpStatus { get; set; }
            public string ResponseTimeS { get; set; }
        }


    }
}
