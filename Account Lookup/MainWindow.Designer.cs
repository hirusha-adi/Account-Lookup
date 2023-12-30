namespace Account_Lookup
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            menuStrip1 = new MenuStrip();
            fileToolStripMenuItem = new ToolStripMenuItem();
            searchToolStripMenuItem = new ToolStripMenuItem();
            clearToolStripMenuItem = new ToolStripMenuItem();
            exitToolStripMenuItem = new ToolStripMenuItem();
            helpToolStripMenuItem = new ToolStripMenuItem();
            guideToolStripMenuItem = new ToolStripMenuItem();
            howItWorksToolStripMenuItem = new ToolStripMenuItem();
            licenseToolStripMenuItem = new ToolStripMenuItem();
            creditsToolStripMenuItem = new ToolStripMenuItem();
            contributeToolStripMenuItem = new ToolStripMenuItem();
            aboutToolStripMenuItem = new ToolStripMenuItem();
            dataGridView1 = new DataGridView();
            groupBox1 = new GroupBox();
            button_clear = new Button();
            button_search = new Button();
            field_username = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label_clear = new Label();
            label4 = new Label();
            label5 = new Label();
            column_id = new DataGridViewTextBoxColumn();
            column_name = new DataGridViewTextBoxColumn();
            column_status = new DataGridViewTextBoxColumn();
            menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // menuStrip1
            // 
            menuStrip1.Items.AddRange(new ToolStripItem[] { fileToolStripMenuItem, helpToolStripMenuItem, aboutToolStripMenuItem });
            menuStrip1.Location = new Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new Size(400, 24);
            menuStrip1.TabIndex = 0;
            menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            fileToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { searchToolStripMenuItem, clearToolStripMenuItem, exitToolStripMenuItem });
            fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            fileToolStripMenuItem.Size = new Size(37, 20);
            fileToolStripMenuItem.Text = "File";
            // 
            // searchToolStripMenuItem
            // 
            searchToolStripMenuItem.Name = "searchToolStripMenuItem";
            searchToolStripMenuItem.Size = new Size(109, 22);
            searchToolStripMenuItem.Text = "Search";
            searchToolStripMenuItem.Click += searchToolStripMenuItem_Click;
            // 
            // clearToolStripMenuItem
            // 
            clearToolStripMenuItem.Name = "clearToolStripMenuItem";
            clearToolStripMenuItem.Size = new Size(109, 22);
            clearToolStripMenuItem.Text = "Clear";
            clearToolStripMenuItem.Click += clearToolStripMenuItem_Click;
            // 
            // exitToolStripMenuItem
            // 
            exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            exitToolStripMenuItem.Size = new Size(109, 22);
            exitToolStripMenuItem.Text = "Exit";
            exitToolStripMenuItem.Click += exitToolStripMenuItem_Click;
            // 
            // helpToolStripMenuItem
            // 
            helpToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { guideToolStripMenuItem, howItWorksToolStripMenuItem, licenseToolStripMenuItem, creditsToolStripMenuItem, contributeToolStripMenuItem });
            helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            helpToolStripMenuItem.Size = new Size(44, 20);
            helpToolStripMenuItem.Text = "Help";
            // 
            // guideToolStripMenuItem
            // 
            guideToolStripMenuItem.Name = "guideToolStripMenuItem";
            guideToolStripMenuItem.Size = new Size(148, 22);
            guideToolStripMenuItem.Text = "Guide";
            guideToolStripMenuItem.Click += guideToolStripMenuItem_Click;
            // 
            // howItWorksToolStripMenuItem
            // 
            howItWorksToolStripMenuItem.Name = "howItWorksToolStripMenuItem";
            howItWorksToolStripMenuItem.Size = new Size(148, 22);
            howItWorksToolStripMenuItem.Text = "How it works?";
            howItWorksToolStripMenuItem.Click += howItWorksToolStripMenuItem_Click;
            // 
            // licenseToolStripMenuItem
            // 
            licenseToolStripMenuItem.Name = "licenseToolStripMenuItem";
            licenseToolStripMenuItem.Size = new Size(148, 22);
            licenseToolStripMenuItem.Text = "License";
            licenseToolStripMenuItem.Click += licenseToolStripMenuItem_Click;
            // 
            // creditsToolStripMenuItem
            // 
            creditsToolStripMenuItem.Name = "creditsToolStripMenuItem";
            creditsToolStripMenuItem.Size = new Size(148, 22);
            creditsToolStripMenuItem.Text = "Credits";
            creditsToolStripMenuItem.Click += creditsToolStripMenuItem_Click;
            // 
            // contributeToolStripMenuItem
            // 
            contributeToolStripMenuItem.Name = "contributeToolStripMenuItem";
            contributeToolStripMenuItem.Size = new Size(148, 22);
            contributeToolStripMenuItem.Text = "Contribute";
            contributeToolStripMenuItem.Click += contributeToolStripMenuItem_Click;
            // 
            // aboutToolStripMenuItem
            // 
            aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            aboutToolStripMenuItem.Size = new Size(52, 20);
            aboutToolStripMenuItem.Text = "About";
            aboutToolStripMenuItem.Click += aboutToolStripMenuItem_Click;
            // 
            // dataGridView1
            // 
            dataGridView1.AllowUserToAddRows = false;
            dataGridView1.AllowUserToDeleteRows = false;
            dataGridView1.AllowUserToOrderColumns = true;
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Columns.AddRange(new DataGridViewColumn[] { column_id, column_name, column_status });
            dataGridView1.Location = new Point(12, 157);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.ReadOnly = true;
            dataGridView1.Size = new Size(375, 254);
            dataGridView1.TabIndex = 1;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(button_clear);
            groupBox1.Controls.Add(button_search);
            groupBox1.Controls.Add(field_username);
            groupBox1.Controls.Add(label1);
            groupBox1.Location = new Point(12, 90);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(375, 61);
            groupBox1.TabIndex = 2;
            groupBox1.TabStop = false;
            groupBox1.Text = "Search";
            // 
            // button_clear
            // 
            button_clear.Location = new Point(339, 22);
            button_clear.Name = "button_clear";
            button_clear.Size = new Size(21, 23);
            button_clear.TabIndex = 3;
            button_clear.Text = "X";
            button_clear.UseVisualStyleBackColor = true;
            // 
            // button_search
            // 
            button_search.Location = new Point(258, 22);
            button_search.Name = "button_search";
            button_search.Size = new Size(75, 23);
            button_search.TabIndex = 2;
            button_search.Text = "Search";
            button_search.UseVisualStyleBackColor = true;
            button_search.Click += button_search_Click;
            // 
            // field_username
            // 
            field_username.Location = new Point(84, 22);
            field_username.Name = "field_username";
            field_username.Size = new Size(168, 23);
            field_username.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(15, 25);
            label1.Name = "label1";
            label1.Size = new Size(63, 15);
            label1.TabIndex = 0;
            label1.Text = "Username:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.ForeColor = SystemColors.Highlight;
            label2.Location = new Point(12, 424);
            label2.Name = "label2";
            label2.Size = new Size(26, 15);
            label2.TabIndex = 3;
            label2.Text = "Exit";
            label2.Click += label2_Click;
            // 
            // label_clear
            // 
            label_clear.AutoSize = true;
            label_clear.ForeColor = SystemColors.Highlight;
            label_clear.Location = new Point(44, 424);
            label_clear.Name = "label_clear";
            label_clear.Size = new Size(34, 15);
            label_clear.TabIndex = 4;
            label_clear.Text = "Clear";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(265, 424);
            label4.Name = "label4";
            label4.Size = new Size(122, 15);
            label4.TabIndex = 5;
            label4.Text = "Made by @hirushaadi";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Segoe UI", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label5.Location = new Point(85, 34);
            label5.Name = "label5";
            label5.Size = new Size(225, 37);
            label5.TabIndex = 6;
            label5.Text = "Account Lookup";
            // 
            // column_id
            // 
            column_id.HeaderText = "ID";
            column_id.Name = "column_id";
            column_id.ReadOnly = true;
            column_id.Width = 10;
            // 
            // column_name
            // 
            column_name.HeaderText = "Platform Name";
            column_name.MinimumWidth = 10;
            column_name.Name = "column_name";
            column_name.ReadOnly = true;
            // 
            // column_status
            // 
            column_status.HeaderText = "Status";
            column_status.Name = "column_status";
            column_status.ReadOnly = true;
            // 
            // MainWindow
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(400, 445);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label_clear);
            Controls.Add(label2);
            Controls.Add(groupBox1);
            Controls.Add(dataGridView1);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            Name = "MainWindow";
            Text = "Account Lookup";
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private MenuStrip menuStrip1;
        private ToolStripMenuItem fileToolStripMenuItem;
        private ToolStripMenuItem searchToolStripMenuItem;
        private ToolStripMenuItem clearToolStripMenuItem;
        private ToolStripMenuItem exitToolStripMenuItem;
        private ToolStripMenuItem helpToolStripMenuItem;
        private ToolStripMenuItem guideToolStripMenuItem;
        private ToolStripMenuItem howItWorksToolStripMenuItem;
        private ToolStripMenuItem licenseToolStripMenuItem;
        private ToolStripMenuItem creditsToolStripMenuItem;
        private ToolStripMenuItem contributeToolStripMenuItem;
        private ToolStripMenuItem aboutToolStripMenuItem;
        private DataGridView dataGridView1;
        private GroupBox groupBox1;
        private Button button_clear;
        private Button button_search;
        private TextBox field_username;
        private Label label1;
        private Label label2;
        private Label label_clear;
        private Label label4;
        private Label label5;
        private DataGridViewTextBoxColumn column_id;
        private DataGridViewTextBoxColumn column_name;
        private DataGridViewTextBoxColumn column_status;
    }
}