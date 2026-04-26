namespace SibercatsLauncher;

partial class MainForm
{
    private System.ComponentModel.IContainer components = null;

    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null)) components.Dispose();
        base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
        // ── top-level tabs ──────────────────────────────────────────────────
        tabMain = new TabControl();
        tabPageConan = new TabPage();
        tabPageExtra = new TabPage();

        // ── Main group ──────────────────────────────────────────────────────
        grpMain = new GroupBox();
        btnStartServer = new Button();
        btnOpenModlist = new Button();
        btnOpenLog = new Button();
        btnDeleteLogs = new Button();

        // ── SQL Database group ──────────────────────────────────────────────
        grpSQL = new GroupBox();
        btnCheckIntegrity = new Button();
        btnOptimize = new Button();
        progressBar = new ProgressBar();

        // ── DB Clean Up group ───────────────────────────────────────────────
        grpDBCleanup = new GroupBox();
        btnScanMods = new Button();
        lblScanStatus = new Label();
        checkedListMods = new CheckedListBox();
        btnSelectAll = new Button();
        btnCleanSelected = new Button();

        // ── Pippi sub-items panel ───────────────────────────────────────────
        grpPippi = new GroupBox();
        checkedListPippi = new CheckedListBox();
        btnSelectAllPippi = new Button();

        // ── Other Tools group ───────────────────────────────────────────────
        grpOtherTools = new GroupBox();
        btnIDStripperTxt = new Button();
        btnIDStripperJson = new Button();
        btnIDStripperCsv = new Button();

        // ── Network group ───────────────────────────────────────────────────
        grpNetwork = new GroupBox();
        lblLocalIP = new Label();
        txtLocalIP = new TextBox();
        lblExternalIP = new Label();
        txtExternalIP = new TextBox();
        networkSeparator = new Label();
        lblPortCheck = new Label();
        txtPorts = new TextBox();
        btnCheckPort = new Button();

        // ═══════════════════════════════════════════════════════════════════
        SuspendLayout();

        // ── Form ────────────────────────────────────────────────────────────
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(942, 555);
        FormBorderStyle = FormBorderStyle.FixedSingle;
        MaximizeBox = false;
        Name = "MainForm";
        Text = "Sibercats Launcher v1.0.0";
        Controls.Add(tabMain);

        // ── tabMain ─────────────────────────────────────────────────────────
        tabMain.Location = new Point(0, 0);
        tabMain.Size = new Size(942, 555);
        tabMain.Controls.Add(tabPageConan);
        tabMain.Controls.Add(tabPageExtra);

        tabPageConan.Text = "Conan Exiles";
        tabPageConan.Controls.Add(grpMain);
        tabPageConan.Controls.Add(grpSQL);
        tabPageConan.Controls.Add(progressBar);
        tabPageConan.Controls.Add(grpDBCleanup);
        tabPageConan.Controls.Add(grpPippi);
        tabPageConan.Controls.Add(grpOtherTools);
        tabPageConan.Controls.Add(grpNetwork);

        tabPageExtra.Text = "Extra";

        // ── grpMain ─────────────────────────────────────────────────────────
        grpMain.Text = "Main:";
        grpMain.Location = new Point(0, 10);
        grpMain.Size = new Size(611, 65);
        grpMain.Controls.Add(btnStartServer);
        grpMain.Controls.Add(btnOpenModlist);
        grpMain.Controls.Add(btnOpenLog);
        grpMain.Controls.Add(btnDeleteLogs);

        btnStartServer.Text = "Start Conan Exiles Server Launcher";
        btnStartServer.Location = new Point(10, 22);
        btnStartServer.Size = new Size(201, 31);

        btnOpenModlist.Text = "Open modlist.txt";
        btnOpenModlist.Location = new Point(220, 22);
        btnOpenModlist.Size = new Size(121, 31);

        btnOpenLog.Text = "Open .log";
        btnOpenLog.Location = new Point(350, 22);
        btnOpenLog.Size = new Size(121, 31);

        btnDeleteLogs.Text = "Delete Saved Logs";
        btnDeleteLogs.Location = new Point(480, 22);
        btnDeleteLogs.Size = new Size(121, 31);

        // ── grpSQL ──────────────────────────────────────────────────────────
        grpSQL.Text = "SQL Database:";
        grpSQL.Location = new Point(1, 90);
        grpSQL.Size = new Size(275, 65);
        grpSQL.Controls.Add(btnCheckIntegrity);
        grpSQL.Controls.Add(btnOptimize);

        btnCheckIntegrity.Text = "Check DB Integrity";
        btnCheckIntegrity.Location = new Point(10, 22);
        btnCheckIntegrity.Size = new Size(121, 31);

        btnOptimize.Text = "Optimize/Vacuum";
        btnOptimize.Location = new Point(140, 22);
        btnOptimize.Size = new Size(121, 31);

        progressBar.Location = new Point(1, 157);
        progressBar.Size = new Size(273, 12);
        progressBar.Visible = false;
        progressBar.Style = ProgressBarStyle.Marquee;
        progressBar.MarqueeAnimationSpeed = 30;

        // ── grpDBCleanup ────────────────────────────────────────────────────
        grpDBCleanup.Text = "DB Clean Up:";
        grpDBCleanup.Location = new Point(1, 170);
        grpDBCleanup.Size = new Size(781, 212);
        grpDBCleanup.Controls.Add(btnScanMods);
        grpDBCleanup.Controls.Add(lblScanStatus);
        grpDBCleanup.Controls.Add(checkedListMods);
        grpDBCleanup.Controls.Add(btnSelectAll);
        grpDBCleanup.Controls.Add(btnCleanSelected);

        btnScanMods.Text = "Scan for Mods";
        btnScanMods.Location = new Point(10, 22);
        btnScanMods.Size = new Size(130, 28);

        lblScanStatus.Text = "Load a game.db to detect installed mods";
        lblScanStatus.Location = new Point(150, 28);
        lblScanStatus.Size = new Size(420, 18);
        lblScanStatus.ForeColor = SystemColors.GrayText;

        checkedListMods.Location = new Point(10, 58);
        checkedListMods.Size = new Size(580, 138);
        checkedListMods.CheckOnClick = true;

        btnSelectAll.Text = "Select All";
        btnSelectAll.Location = new Point(600, 58);
        btnSelectAll.Size = new Size(165, 28);

        btnCleanSelected.Text = "Clean Selected Mods";
        btnCleanSelected.Location = new Point(600, 175);
        btnCleanSelected.Size = new Size(165, 28);

        // ── grpPippi (hidden until Pippi is checked) ────────────────────────
        grpPippi.Text = "Pippi Sub-Items:";
        grpPippi.Location = new Point(1, 384);
        grpPippi.Size = new Size(781, 115);
        grpPippi.Visible = false;
        grpPippi.Controls.Add(checkedListPippi);
        grpPippi.Controls.Add(btnSelectAllPippi);

        checkedListPippi.Location = new Point(5, 18);
        checkedListPippi.Size = new Size(680, 85);
        checkedListPippi.CheckOnClick = true;
        checkedListPippi.MultiColumn = true;
        checkedListPippi.ColumnWidth = 110;

        btnSelectAllPippi.Text = "Select All";
        btnSelectAllPippi.Location = new Point(693, 46);
        btnSelectAllPippi.Size = new Size(80, 28);

        // ── grpOtherTools ───────────────────────────────────────────────────
        grpOtherTools.Text = "Other Tools:";
        grpOtherTools.Location = new Point(770, 10);
        grpOtherTools.Size = new Size(175, 141);
        grpOtherTools.Controls.Add(btnIDStripperTxt);
        grpOtherTools.Controls.Add(btnIDStripperJson);
        grpOtherTools.Controls.Add(btnIDStripperCsv);

        btnIDStripperTxt.Text = "ID Stripper {.txt Column}";
        btnIDStripperTxt.Location = new Point(10, 20);
        btnIDStripperTxt.Size = new Size(155, 31);

        btnIDStripperJson.Text = "ID Stripper {.json}";
        btnIDStripperJson.Location = new Point(10, 60);
        btnIDStripperJson.Size = new Size(155, 31);

        btnIDStripperCsv.Text = "ID Stripper {.csv}";
        btnIDStripperCsv.Location = new Point(10, 100);
        btnIDStripperCsv.Size = new Size(155, 31);

        // ── grpNetwork ──────────────────────────────────────────────────────
        grpNetwork.Text = "Network";
        grpNetwork.Location = new Point(790, 170);
        grpNetwork.Size = new Size(141, 212);
        grpNetwork.Controls.Add(lblLocalIP);
        grpNetwork.Controls.Add(txtLocalIP);
        grpNetwork.Controls.Add(lblExternalIP);
        grpNetwork.Controls.Add(txtExternalIP);
        grpNetwork.Controls.Add(networkSeparator);
        grpNetwork.Controls.Add(lblPortCheck);
        grpNetwork.Controls.Add(txtPorts);
        grpNetwork.Controls.Add(btnCheckPort);

        lblLocalIP.Text = "Ipv4 Address Local:";
        lblLocalIP.Location = new Point(15, 20);
        lblLocalIP.Size = new Size(121, 20);
        lblLocalIP.Font = new Font(lblLocalIP.Font.FontFamily, 10);

        txtLocalIP.Location = new Point(15, 40);
        txtLocalIP.Size = new Size(113, 20);
        txtLocalIP.ReadOnly = true;

        lblExternalIP.Text = "External IP:";
        lblExternalIP.Location = new Point(15, 65);
        lblExternalIP.Size = new Size(81, 20);
        lblExternalIP.Font = new Font(lblExternalIP.Font.FontFamily, 10);

        txtExternalIP.Location = new Point(15, 85);
        txtExternalIP.Size = new Size(113, 20);
        txtExternalIP.ReadOnly = true;

        networkSeparator.BorderStyle = BorderStyle.Fixed3D;
        networkSeparator.Location = new Point(0, 112);
        networkSeparator.Size = new Size(141, 2);

        lblPortCheck.Text = "Check Port Being Used:";
        lblPortCheck.Location = new Point(11, 120);
        lblPortCheck.Size = new Size(131, 20);

        txtPorts.Location = new Point(15, 140);
        txtPorts.Size = new Size(113, 20);
        txtPorts.PlaceholderText = "UDP/TCP Port";
        txtPorts.ToolTip("Check if the given port on UDP and TCP is being used.\r\nSeparate multiple ports with commas: 7777,27015");

        btnCheckPort.Text = "Check Port";
        btnCheckPort.Location = new Point(30, 170);
        btnCheckPort.Size = new Size(75, 23);

        ResumeLayout(false);
    }

    // ── Controls ─────────────────────────────────────────────────────────────
    private TabControl tabMain;
    private TabPage tabPageConan, tabPageExtra;

    private GroupBox grpMain;
    private Button btnStartServer, btnOpenModlist, btnOpenLog, btnDeleteLogs;

    private GroupBox grpSQL;
    private Button btnCheckIntegrity, btnOptimize;
    private ProgressBar progressBar;

    private GroupBox grpDBCleanup;
    private Button btnScanMods, btnSelectAll, btnCleanSelected;
    private Label lblScanStatus;
    private CheckedListBox checkedListMods;

    private GroupBox grpPippi;
    private CheckedListBox checkedListPippi;
    private Button btnSelectAllPippi;

    private GroupBox grpOtherTools;
    private Button btnIDStripperTxt, btnIDStripperJson, btnIDStripperCsv;

    private GroupBox grpNetwork;
    private Label lblLocalIP, lblExternalIP, lblPortCheck;
    private TextBox txtLocalIP, txtExternalIP, txtPorts;
    private Label networkSeparator;
    private Button btnCheckPort;
}

internal static class ControlExtensions
{
    private static readonly ToolTip _tip = new();
    public static void ToolTipText(this Button b, string text) => _tip.SetToolTip(b, text);
    public static void ToolTip(this TextBox t, string text) => _tip.SetToolTip(t, text);
}
