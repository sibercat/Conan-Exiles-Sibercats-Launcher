using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.RegularExpressions;

namespace SibercatsLauncher;

public partial class MainForm : Form
{
    private static readonly string CfgPath =
        Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "launcher.cfg");

    private static readonly string Sqlite3 =
        Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "sqlite3.exe");

    private string? _serverBaseDir;
    private string? _loadedDbPath;
    private readonly Dictionary<string, (string actor, string blob)> _modPatterns = new();

    private static readonly (string display, string actorSuffix)[] PippiComponents =
    [
        ("Wallpaper",    "Pippi_Wallpaper"),
        ("Glorb",        "Pippi_Glorb"),
        ("NPC Spawner",  "Pippi_NPCSpawner"),
        ("Loot Spawner", "Pippi_LootSpawner"),
        ("Portal",       "Pippi_Warper"),
        ("Flaggi",       "Pippi_Flaggi"),
        ("Thespian",     "Pippi_Mob"),
        ("Egress",       "Pippi_Egress"),
        ("CamLoc",       "Pippi_CamLoc"),
        ("Pippijack",    "Pippi_BlackJack"),
        ("Pippi Note",   "Pippi_Note"),
        ("MusiqBox",     "Pippi_MusicBox"),
        ("TZone",        "Blueprints/PippiTools/TZone/BP_TZone"),
        ("TTime",        "Blueprints/PippiTools/TTime/BP_TTime"),
        ("TControl",     "Blueprints/PippiTools/TControl"),
        ("TPlatform",    "Blueprints/PippiTools/TPlatform/BP_TPlatform"),
        ("TSeq",         "Blueprints/PippiTools/TSeq/BP_TSeq"),
        ("TRand",        "Blueprints/PippiTools/TRand/BP_TRand"),
        ("TPlate",       "Blueprints/PippiTools/TPlate/BP_TPlate"),
        ("TCombiner",    "Blueprints/PippiTools/TCombiner/BP_TCombiner"),
        ("Marker",       "Blueprints/PippiTools/Marker/BP_Marker"),
        ("RePlaceable",  "Blueprints/PippiTools/Replaceable/BP_RePlaceable"),
        ("NPC Summoner", "Blueprints/PippiTools/NPCSummoner/BP_NPCSummoner"),
        ("Easel",        "Blueprints/PippiTools/Easel/BP_Easel"),
        ("Lazor",        "Blueprints/PippiTools/Lazor/BP_Lazor"),
        ("Cryptex",      "Blueprints/PippiTools/Cryptex/BP_Cryptex"),
        ("Checkpoint",   "Blueprints/PippiTools/Checkpoint/BP_Checkpoint"),
    ];

    // ── Server path resolution ────────────────────────────────────────────────

    private string? ServerBaseDir
    {
        get
        {
            if (_serverBaseDir != null) return _serverBaseDir;

            var appDir = AppDomain.CurrentDomain.BaseDirectory;
            if (File.Exists(Path.Combine(appDir, "DedicatedServerLauncher.exe")))
                return _serverBaseDir = appDir;

            if (File.Exists(CfgPath))
            {
                var saved = File.ReadAllText(CfgPath).Trim();
                if (File.Exists(Path.Combine(saved, "DedicatedServerLauncher.exe")))
                    return _serverBaseDir = saved;
            }

            return null;
        }
    }

    private string? ResolveServerBaseDir()
    {
        if (ServerBaseDir != null) return ServerBaseDir;

        var answer = MessageBox.Show(
            "Could not find DedicatedServerLauncher.exe.\n\nWould you like to browse for it?",
            "File Not Found", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

        if (answer != DialogResult.Yes) return null;

        using var dlg = new OpenFileDialog
        {
            Title  = "Locate DedicatedServerLauncher.exe",
            Filter = "Executable files (*.exe)|*.exe",
        };

        if (dlg.ShowDialog() != DialogResult.OK) return null;

        _serverBaseDir = Path.GetDirectoryName(dlg.FileName)!;
        File.WriteAllText(CfgPath, _serverBaseDir);
        return _serverBaseDir;
    }

    private static string ModlistPath(string baseDir) =>
        Path.Combine(baseDir, "DedicatedServerLauncher", "ConanExilesDedicatedServer", "ConanSandbox", "Mods", "modlist.txt");

    private static string LogFilePath(string baseDir) =>
        Path.Combine(baseDir, "DedicatedServerLauncher", "ConanExilesDedicatedServer", "ConanSandbox", "Saved", "Logs", "ConanSandbox.log");

    private static string LogFolderPath(string baseDir) =>
        Path.Combine(baseDir, "DedicatedServerLauncher", "ConanExilesDedicatedServer", "ConanSandbox", "Saved", "Logs");

    // ── Constructor ───────────────────────────────────────────────────────────

    public MainForm()
    {
        InitializeComponent();

        btnStartServer.Click       += (_, _) => OpenDedicatedServer();
        btnOpenModlist.Click       += (_, _) => OpenModlist();
        btnOpenLog.Click           += (_, _) => OpenLogFile();
        btnDeleteLogs.Click        += (_, _) => DeleteLogFiles();
        btnCheckIntegrity.Click    += (_, _) => CheckDatabaseIntegrity();
        btnOptimize.Click          += (_, _) => OptimizeDatabase();
        btnScanMods.Click          += (_, _) => ScanForMods();
        checkedListMods.ItemCheck  += (s, e) => OnModItemCheck(s, e);
        btnSelectAll.Click         += (_, _) => ToggleSelectAll();
        btnCleanSelected.Click     += (_, _) => CleanSelectedMods();
        btnSelectAllPippi.Click    += (_, _) => ToggleSelectAllPippi();
        btnIDStripperTxt.Click     += (_, _) => IdStripperTxt();
        btnIDStripperJson.Click    += (_, _) => IdStripperJson();
        btnIDStripperCsv.Click     += (_, _) => IdStripperCsv();
        btnCheckPort.Click         += (_, _) => CheckPort();

        SetLocalIpv4();
        _ = UpdateExternalIpAsync();
    }

    // ── SQLite via sqlite3.exe ────────────────────────────────────────────────

    private static (int exitCode, string stdout, string stderr) RunSqlite(string dbPath, string sql)
    {
        var psi = new ProcessStartInfo(Sqlite3, $"\"{dbPath}\"")
        {
            RedirectStandardInput  = true,
            RedirectStandardOutput = true,
            RedirectStandardError  = true,
            UseShellExecute        = false,
            CreateNoWindow         = true
        };
        using var proc = Process.Start(psi)!;
        proc.StandardInput.WriteLine(sql);
        proc.StandardInput.Close();
        proc.WaitForExit();
        return (proc.ExitCode, proc.StandardOutput.ReadToEnd().Trim(), proc.StandardError.ReadToEnd().Trim());
    }

    // ── DB Clean Up — dynamic mod detection ──────────────────────────────────
    // _pippiPatterns: display name → (actorLikePattern, blobSearchPath) for Pippi sub-items
    private readonly Dictionary<string, (string actor, string blob)> _pippiPatterns = new();

    private void ScanForMods()
    {
        var path = PickDbFile("Select game.db to scan");
        if (path == null) return;

        _loadedDbPath = path;
        checkedListMods.Items.Clear();
        checkedListPippi.Items.Clear();
        _modPatterns.Clear();
        _pippiPatterns.Clear();
        grpPippi.Visible = false;

        var sql = @"
SELECT DISTINCT
  SUBSTR(class,
    INSTR(class, '/Game/Mods/') + 11,
    CASE
      WHEN INSTR(SUBSTR(class, INSTR(class, '/Game/Mods/') + 11), '/') > 0
      THEN INSTR(SUBSTR(class, INSTR(class, '/Game/Mods/') + 11), '/') - 1
      ELSE LENGTH(class)
    END
  ) AS mod_name
FROM actor_position
WHERE class LIKE '%/Game/Mods/%'
ORDER BY mod_name;";

        var (_, stdout, stderr) = RunSqlite(path, sql);

        if (!string.IsNullOrEmpty(stderr))
        {
            MessageBox.Show($"Error scanning database:\n{stderr}", "Scan Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        var mods = stdout
            .Split('\n', StringSplitOptions.RemoveEmptyEntries)
            .Select(l => l.Trim())
            .Where(l => !string.IsNullOrEmpty(l))
            .ToList();

        if (mods.Count == 0)
        {
            lblScanStatus.Text = "No mod content found in this database.";
            lblScanStatus.ForeColor = SystemColors.GrayText;
            return;
        }

        bool pippiFound = false;
        foreach (var mod in mods)
        {
            if (mod.Equals("Pippi", StringComparison.OrdinalIgnoreCase))
            {
                // Detect which Pippi sub-components are present
                var checkSql = new StringBuilder();
                foreach (var (display, suffix) in PippiComponents)
                {
                    var p = $"%/Game/Mods/Pippi/{suffix}%";
                    checkSql.AppendLine($"SELECT '{display}' WHERE EXISTS (SELECT 1 FROM actor_position WHERE class LIKE '{p}');");
                }
                var (_, pippiOut, _) = RunSqlite(path, checkSql.ToString());
                var found = pippiOut
                    .Split('\n', StringSplitOptions.RemoveEmptyEntries)
                    .Select(l => l.Trim())
                    .Where(l => !string.IsNullOrEmpty(l))
                    .ToHashSet();

                foreach (var (display, suffix) in PippiComponents)
                {
                    if (!found.Contains(display)) continue;
                    _pippiPatterns[display] = ($"%/Game/Mods/Pippi/{suffix}%", $"/Game/Mods/Pippi/{suffix}");
                    checkedListPippi.Items.Add(display);
                }

                if (checkedListPippi.Items.Count > 0)
                {
                    // Add Pippi as a single top-level entry; sub-panel reveals on check
                    _modPatterns["Pippi"] = ("%/Game/Mods/Pippi/%", "/Game/Mods/Pippi/");
                    checkedListMods.Items.Add("Pippi");
                    pippiFound = true;
                }
            }
            else
            {
                _modPatterns[mod] = ($"%/Game/Mods/{mod}/%", $"/Game/Mods/{mod}/");
                checkedListMods.Items.Add(mod);
            }
        }

        var total = checkedListMods.Items.Count;
        var suffix2 = pippiFound ? $" (Pippi has {checkedListPippi.Items.Count} sub-items)" : "";
        lblScanStatus.Text = $"Found {total} mod(s) in {Path.GetFileName(path)}{suffix2}";
        lblScanStatus.ForeColor = Color.DarkGreen;
    }

    private void OnModItemCheck(object? sender, ItemCheckEventArgs e)
    {
        // ItemCheck fires BEFORE state changes — use BeginInvoke to read new state
        BeginInvoke(() =>
        {
            var item = checkedListMods.Items[e.Index]?.ToString();
            if (item == "Pippi")
            {
                bool isChecked = checkedListMods.GetItemChecked(e.Index);
                grpPippi.Visible = isChecked;
                if (isChecked)
                {
                    // Pre-check all Pippi sub-items when Pippi is selected
                    for (int i = 0; i < checkedListPippi.Items.Count; i++)
                        checkedListPippi.SetItemChecked(i, true);
                    btnSelectAllPippi.Text = "Deselect All";
                }
                else
                {
                    for (int i = 0; i < checkedListPippi.Items.Count; i++)
                        checkedListPippi.SetItemChecked(i, false);
                    btnSelectAllPippi.Text = "Select All";
                }
            }
            UpdateSelectionStatus();
        });
    }

    private void ToggleSelectAll()
    {
        bool allChecked = checkedListMods.CheckedItems.Count == checkedListMods.Items.Count;
        for (int i = 0; i < checkedListMods.Items.Count; i++)
            checkedListMods.SetItemChecked(i, !allChecked);

        btnSelectAll.Text = allChecked ? "Select All" : "Deselect All";
        UpdateSelectionStatus();
    }

    private void ToggleSelectAllPippi()
    {
        bool allChecked = checkedListPippi.CheckedItems.Count == checkedListPippi.Items.Count;
        for (int i = 0; i < checkedListPippi.Items.Count; i++)
            checkedListPippi.SetItemChecked(i, !allChecked);
        btnSelectAllPippi.Text = allChecked ? "Select All" : "Deselect All";
    }

    private void UpdateSelectionStatus()
    {
        int count = checkedListMods.CheckedItems.Count;
        if (count == 0)
        {
            lblScanStatus.Text = $"Found {checkedListMods.Items.Count} mod(s) — none selected";
            lblScanStatus.ForeColor = SystemColors.GrayText;
        }
        else
        {
            var names = checkedListMods.CheckedItems.Cast<string>().ToList();
            // If Pippi is checked, append how many sub-items are selected
            if (names.Contains("Pippi") && grpPippi.Visible)
            {
                int pippiSel = checkedListPippi.CheckedItems.Count;
                names[names.IndexOf("Pippi")] = $"Pippi ({pippiSel} sub-items)";
            }
            lblScanStatus.Text = $"{count} selected: {string.Join(", ", names)}";
            lblScanStatus.ForeColor = Color.DarkOrange;
        }
    }

    private void CleanSelectedMods()
    {
        if (_loadedDbPath == null || checkedListMods.Items.Count == 0)
        {
            MessageBox.Show("Please scan a database first.", "No Database",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        var selected = checkedListMods.CheckedItems.Cast<string>().ToList();
        if (selected.Count == 0)
        {
            MessageBox.Show("Please select at least one mod to clean.", "Nothing Selected",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        var confirm = MessageBox.Show(
            $"This will remove all data for the following mod(s) from the database:\n\n" +
            string.Join("\n", selected.Select(m => $"  • {m}")) +
            "\n\nThis cannot be undone. Continue?",
            "Confirm Cleanup", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

        if (confirm != DialogResult.Yes) return;

        var sql = new StringBuilder();
        foreach (var mod in selected)
        {
            if (mod == "Pippi" && grpPippi.Visible)
            {
                // Clean only the checked Pippi sub-items
                foreach (var sub in checkedListPippi.CheckedItems.Cast<string>())
                {
                    if (!_pippiPatterns.TryGetValue(sub, out var pp)) continue;
                    var (pp_pat, pp_blob) = pp;
                    sql.AppendLine($"DELETE FROM item_inventory WHERE owner_id IN (SELECT id FROM actor_position WHERE class LIKE '{pp_pat}');");
                    sql.AppendLine($"DELETE FROM item_inventory WHERE INSTR(data, '{pp_blob}') > 0;");
                    sql.AppendLine($"DELETE FROM properties WHERE object_id IN (SELECT id FROM actor_position WHERE class LIKE '{pp_pat}');");
                    sql.AppendLine($"DELETE FROM building_instances WHERE class LIKE '{pp_pat}';");
                    sql.AppendLine($"DELETE FROM actor_position WHERE class LIKE '{pp_pat}';");
                }
            }
            else
            {
                if (!_modPatterns.TryGetValue(mod, out var pat)) continue;
                var (pattern, blobPath) = pat;
                sql.AppendLine($"DELETE FROM item_inventory WHERE owner_id IN (SELECT id FROM actor_position WHERE class LIKE '{pattern}');");
                sql.AppendLine($"DELETE FROM item_inventory WHERE INSTR(data, '{blobPath}') > 0;");
                sql.AppendLine($"DELETE FROM properties WHERE object_id IN (SELECT id FROM actor_position WHERE class LIKE '{pattern}');");
                sql.AppendLine($"DELETE FROM building_instances WHERE class LIKE '{pattern}';");
                sql.AppendLine($"DELETE FROM actor_position WHERE class LIKE '{pattern}';");
            }
        }

        var (_, _, stderr) = RunSqlite(_loadedDbPath, sql.ToString());

        if (!string.IsNullOrEmpty(stderr))
        {
            MessageBox.Show($"An error occurred:\n{stderr}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        MessageBox.Show(
            "Cleanup complete. It is recommended to run Optimize/Vacuum afterwards.",
            "Done", MessageBoxButtons.OK, MessageBoxIcon.Information);

        // Re-scan to refresh the list
        var (_, stdout2, _) = RunSqlite(_loadedDbPath, @"
SELECT DISTINCT
  SUBSTR(class,
    INSTR(class, '/Game/Mods/') + 11,
    CASE
      WHEN INSTR(SUBSTR(class, INSTR(class, '/Game/Mods/') + 11), '/') > 0
      THEN INSTR(SUBSTR(class, INSTR(class, '/Game/Mods/') + 11), '/') - 1
      ELSE LENGTH(class)
    END
  ) AS mod_name
FROM actor_position
WHERE class LIKE '%/Game/Mods/%'
ORDER BY mod_name;");

        checkedListMods.Items.Clear();
        var remaining = stdout2.Split('\n', StringSplitOptions.RemoveEmptyEntries)
            .Select(l => l.Trim()).Where(l => !string.IsNullOrEmpty(l)).ToList();

        foreach (var mod in remaining)
            checkedListMods.Items.Add(mod);

        lblScanStatus.Text = remaining.Count == 0
            ? "No mod content remaining."
            : $"{remaining.Count} mod(s) remaining in {Path.GetFileName(_loadedDbPath)}";
        lblScanStatus.ForeColor = remaining.Count == 0 ? Color.DarkGreen : SystemColors.ControlText;
    }

    // ── Database Operations ───────────────────────────────────────────────────

    private void CheckDatabaseIntegrity()
    {
        var path = PickDbFile("Select Database File");
        if (path == null) return;

        var (_, stdout, stderr) = RunSqlite(path, "PRAGMA integrity_check;");

        if (!string.IsNullOrEmpty(stderr))
        {
            MessageBox.Show($"Error connecting to the database: {stderr}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        if (stdout == "ok")
        {
            MessageBox.Show("The database integrity is OK.", "Database Integrity Check",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        // Integrity check found issues — offer recovery inline
        var issues = stdout.Length > 800 ? stdout[..800] + "\n...(truncated)" : stdout;
        var answer = MessageBox.Show(
            $"Integrity check found issues:\n\n{issues}\n\n" +
            "Would you like to attempt recovery?\n" +
            "A recovered copy will be saved as [filename]_recovered.db next to the original.\n" +
            "Your original file will not be modified.",
            "Database Corruption Detected",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Warning);

        if (answer == DialogResult.Yes)
            RecoverDatabase(path);
    }

    private void OptimizeDatabase()
    {
        var path = PickDbFile("Select Database File");
        if (path == null) return;

        progressBar.Visible = true;
        btnOptimize.Enabled = false;

        Task.Run(() =>
        {
            var (_, _, stderr) = RunSqlite(path, "PRAGMA optimize;\nVACUUM;");
            Invoke(() =>
            {
                progressBar.Visible = false;
                btnOptimize.Enabled = true;
                if (!string.IsNullOrEmpty(stderr))
                    MessageBox.Show($"An error occurred: {stderr}", "Database Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                else
                    MessageBox.Show("The database has been optimized successfully.", "Database Optimized",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
            });
        });
    }

    private void RecoverDatabase(string dbPath)
    {
        progressBar.Visible = true;
        btnCheckIntegrity.Enabled = false;

        Task.Run(() =>
        {
            var dir          = Path.GetDirectoryName(dbPath)!;
            var nameNoExt    = Path.GetFileNameWithoutExtension(dbPath);
            var recoveredPath = Path.Combine(dir, $"{nameNoExt}_recovered.db");

            if (File.Exists(recoveredPath)) File.Delete(recoveredPath);

            string result;
            try
            {
                // Step 1: sqlite3.exe corrupt.db .recover → SQL statements
                var psi1 = new ProcessStartInfo(Sqlite3, $"\"{dbPath}\" .recover")
                {
                    RedirectStandardOutput = true,
                    RedirectStandardError  = true,
                    UseShellExecute        = false,
                    CreateNoWindow         = true
                };
                using var proc1 = Process.Start(psi1)!;
                var recoverSql = proc1.StandardOutput.ReadToEnd();
                var err1       = proc1.StandardError.ReadToEnd();
                proc1.WaitForExit();

                if (proc1.ExitCode != 0 && string.IsNullOrWhiteSpace(recoverSql))
                {
                    result = $"Recovery failed — could not read source database:\n{err1}";
                }
                else
                {
                    // Step 2: pipe that SQL into a new database file
                    var psi2 = new ProcessStartInfo(Sqlite3, $"\"{recoveredPath}\"")
                    {
                        RedirectStandardInput  = true,
                        RedirectStandardOutput = true,
                        RedirectStandardError  = true,
                        UseShellExecute        = false,
                        CreateNoWindow         = true
                    };
                    using var proc2 = Process.Start(psi2)!;
                    proc2.StandardInput.Write(recoverSql);
                    proc2.StandardInput.Close();
                    var err2 = proc2.StandardError.ReadToEnd();
                    proc2.WaitForExit();

                    result = (proc2.ExitCode == 0 && string.IsNullOrWhiteSpace(err2))
                        ? $"Recovery complete.\n\nSaved to:\n{recoveredPath}\n\nStop the server, replace game.db with the recovered file, then restart."
                        : $"Recovery finished with warnings:\n{err2}\n\nPartial file saved to:\n{recoveredPath}";
                }
            }
            catch (Exception ex)
            {
                result = $"Exception during recovery: {ex.Message}";
            }

            Invoke(() =>
            {
                progressBar.Visible = false;
                btnCheckIntegrity.Enabled = true;
                var icon = result.StartsWith("Recovery complete") ? MessageBoxIcon.Information : MessageBoxIcon.Warning;
                MessageBox.Show(result, "Recovery Finished", MessageBoxButtons.OK, icon);
            });
        });
    }

    // ── Network ───────────────────────────────────────────────────────────────

    private void SetLocalIpv4()
    {
        try
        {
            var host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (var addr in host.AddressList)
            {
                if (addr.AddressFamily == AddressFamily.InterNetwork)
                {
                    txtLocalIP.Text = addr.ToString();
                    return;
                }
            }
        }
        catch { }
    }

    private async Task UpdateExternalIpAsync()
    {
        try
        {
            using var client = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };
            var json  = await client.GetStringAsync("https://api.ipify.org?format=json");
            var match = Regex.Match(json, @"""ip""\s*:\s*""([^""]+)""");
            if (match.Success)
                txtExternalIP.Text = match.Groups[1].Value;
        }
        catch (Exception ex)
        {
            txtExternalIP.Text = $"Error: {ex.Message}";
        }
    }

    private void CheckPort()
    {
        var portsStr = txtPorts.Text.Trim();
        if (string.IsNullOrEmpty(portsStr))
        {
            MessageBox.Show("Please enter at least one port number.", "Input Error",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        var parts = portsStr.Split(',');
        if (!parts.All(p => int.TryParse(p.Trim(), out _)))
        {
            MessageBox.Show("Please enter only numeric port values.", "Input Error",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        var ports   = parts.Select(p => int.Parse(p.Trim())).ToArray();
        var localIP = txtLocalIP.Text;

        foreach (var protocol in new[] { "UDP", "TCP" })
        {
            var used   = new List<int>();
            var unused = new List<int>();

            foreach (var port in ports)
            {
                if (IsPortInUse(port, protocol, localIP)) used.Add(port);
                else unused.Add(port);
            }

            if (used.Count > 0)
                MessageBox.Show($"The following {protocol} ports are being used: {string.Join(", ", used)}",
                    $"{protocol} Ports Used", MessageBoxButtons.OK, MessageBoxIcon.Information);
            if (unused.Count > 0)
                MessageBox.Show($"The following {protocol} ports are not being used: {string.Join(", ", unused)}",
                    $"{protocol} Ports Not Used", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }

    private static bool IsPortInUse(int port, string protocol, string localIP)
    {
        try
        {
            if (protocol == "UDP")
            {
                using var sock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
                sock.Bind(new IPEndPoint(IPAddress.Parse(localIP), port));
                return false;
            }
            else
            {
                using var client = new TcpClient();
                var result  = client.BeginConnect(localIP, port, null, null);
                var success = result.AsyncWaitHandle.WaitOne(TimeSpan.FromSeconds(1));
                if (success) client.EndConnect(result);
                return success;
            }
        }
        catch { return true; }
    }

    // ── Server / File Operations ──────────────────────────────────────────────

    private void OpenDedicatedServer()
    {
        var baseDir = ResolveServerBaseDir();
        if (baseDir == null) return;

        Process.Start(new ProcessStartInfo(Path.Combine(baseDir, "DedicatedServerLauncher.exe"))
            { UseShellExecute = true });
    }

    private void OpenModlist()
    {
        var baseDir = ResolveServerBaseDir();
        if (baseDir == null) return;

        var path = ModlistPath(baseDir);
        if (File.Exists(path))
            Process.Start(new ProcessStartInfo("notepad.exe", path) { UseShellExecute = true });
        else
            MessageBox.Show($"Could not find modlist.txt at:\n{path}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
    }

    private void OpenLogFile()
    {
        var baseDir = ResolveServerBaseDir();
        if (baseDir == null) return;

        var path = LogFilePath(baseDir);
        if (File.Exists(path))
            Process.Start(new ProcessStartInfo("notepad.exe", path) { UseShellExecute = true });
        else
            MessageBox.Show($"Could not find ConanSandbox.log at:\n{path}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
    }

    private void DeleteLogFiles()
    {
        var baseDir = ResolveServerBaseDir();
        if (baseDir == null) return;

        var folder = LogFolderPath(baseDir);
        if (!Directory.Exists(folder))
        {
            MessageBox.Show($"Could not find log folder at:\n{folder}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        if (Process.GetProcessesByName("ConanSandboxServer").Length > 0)
        {
            MessageBox.Show("ConanSandboxServer.exe is running. Cannot delete log files.",
                "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        foreach (var file in Directory.GetFiles(folder, "*.log"))
            File.Delete(file);

        MessageBox.Show("Log files deleted successfully.", "Log Files Deleted",
            MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    // ── ID Strippers ──────────────────────────────────────────────────────────
    // All three produce ('id1','id2',...) saved next to the source file as output_ids.txt

    private static string IdOutputPath(string inputFile) =>
        Path.Combine(Path.GetDirectoryName(inputFile)!, "output_ids.txt");

    private void IdStripperTxt()
    {
        using var dlg = new OpenFileDialog { Filter = "Text files (*.txt)|*.txt" };
        if (dlg.ShowDialog() != DialogResult.OK) return;

        try
        {
            var text    = File.ReadAllText(dlg.FileName);
            var ids     = Regex.Matches(text, @"\d+").Select(m => $"'{m.Value}'");
            var outPath = IdOutputPath(dlg.FileName);
            File.WriteAllText(outPath, $"({string.Join(",", ids)})", Encoding.UTF8);
            MessageBox.Show($"IDs extracted and saved to:\n{outPath}",
                "Extraction Complete", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        catch (Exception ex)
        {
            MessageBox.Show($"An error occurred: {ex.Message}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

    private void IdStripperJson()
    {
        using var dlg = new OpenFileDialog { Filter = "JSON files (*.json)|*.json" };
        if (dlg.ShowDialog() != DialogResult.OK) return;

        try
        {
            var enc  = DetectEncoding(dlg.FileName);
            var ids  = new List<string>();

            foreach (var line in File.ReadLines(dlg.FileName, enc))
            {
                if (line.IndexOf("RowName", StringComparison.Ordinal) < 0) continue;
                var parts = line.Trim().Split(": ");
                if (parts.Length >= 2)
                    ids.Add($"'{parts[1].Trim('"', ',', ' ')}'");
            }

            if (ids.Count == 0)
            {
                MessageBox.Show("No RowName entries found in this JSON file.",
                    "Nothing Found", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            var outPath = IdOutputPath(dlg.FileName);
            File.WriteAllText(outPath, $"({string.Join(",", ids)})", Encoding.UTF8);
            MessageBox.Show($"{ids.Count} IDs extracted and saved to:\n{outPath}",
                "Extraction Complete", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        catch (Exception ex)
        {
            MessageBox.Show($"An error occurred: {ex.Message}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

    private void IdStripperCsv()
    {
        using var dlg = new OpenFileDialog { Filter = "CSV files (*.csv)|*.csv" };
        if (dlg.ShowDialog() != DialogResult.OK) return;

        try
        {
            var enc = DetectEncoding(dlg.FileName);
            var ids = new List<string>();

            foreach (var line in File.ReadLines(dlg.FileName, enc))
            {
                if (string.IsNullOrWhiteSpace(line)) continue;
                var m = Regex.Match(line.Split(',')[0], @"^\d+");
                if (m.Success) ids.Add($"'{m.Value}'");
            }

            if (ids.Count == 0)
            {
                MessageBox.Show("No numeric IDs found at the start of the first column.",
                    "Nothing Found", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            var outPath = IdOutputPath(dlg.FileName);
            File.WriteAllText(outPath, $"({string.Join(",", ids)})", Encoding.UTF8);
            MessageBox.Show($"{ids.Count} IDs extracted and saved to:\n{outPath}",
                "Extraction Complete", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        catch (Exception ex)
        {
            MessageBox.Show($"An error occurred: {ex.Message}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

    // ── Helpers ───────────────────────────────────────────────────────────────

    private static string? PickDbFile(string title)
    {
        using var dlg = new OpenFileDialog { Title = title, Filter = "Database files (*.db)|*.db" };
        return dlg.ShowDialog() == DialogResult.OK ? dlg.FileName : null;
    }

    private static Encoding DetectEncoding(string filePath)
    {
        var bom = new byte[4];
        using var fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
        fs.ReadExactly(bom, 0, 4);
        if (bom[0] == 0xEF && bom[1] == 0xBB && bom[2] == 0xBF) return Encoding.UTF8;
        if (bom[0] == 0xFF && bom[1] == 0xFE) return Encoding.Unicode;
        if (bom[0] == 0xFE && bom[1] == 0xFF) return Encoding.BigEndianUnicode;
        return Encoding.UTF8;
    }
}
