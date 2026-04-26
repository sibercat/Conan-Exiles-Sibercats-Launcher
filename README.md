# Sibercats Launcher v1.0.0

A Windows desktop tool for managing Conan Exiles dedicated servers. Built with C# / .NET 10 WinForms.

## Requirements

- [.NET 10 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) (Desktop Runtime)
- `sqlite3.exe` — included in the release

![Dashboard](https://raw.githubusercontent.com/sibercat/Conan-Exiles-Sibercats-Launcher/refs/heads/main/preview.webp)

Executable can be found here [Releases](https://github.com/sibercat/Conan-Exiles-Sibercats-Launcher/releases)

## Features

### Main
- Launch the Conan Exiles Dedicated Server Launcher
- Open `modlist.txt` directly in Notepad
- Open the server log (`ConanSandbox.log`)
- Delete saved log files

### SQL Database
- **Check DB Integrity** — runs `PRAGMA integrity_check`. If corruption is detected, offers to attempt recovery and saves a `_recovered.db` copy next to the original
- **Optimize/Vacuum** — runs `PRAGMA optimize` + `VACUUM` in the background to defrag and shrink the database

### DB Clean Up
- **Scan for Mods** — loads a `game.db` and detects all installed mods from `actor_position` class paths
- Select individual mods to remove their data (actors, properties, inventories, building instances)
- **Pippi** expands into individual sub-items (Wallpaper, Glorb, Egress, Warper, etc.) so you can clean specific components

### Other Tools
- **ID Stripper** — extracts numeric IDs from `.txt`, `.json` (RowName), or `.csv` files and outputs them as a SQL-ready `('id1','id2',...)` list saved next to the source file

### Network
- Displays local IPv4 and external IP
- Check if a UDP/TCP port is in use

## Building

```
dotnet publish -c Release -o bin/publish-final
```

Output: `SibercatsLauncher.exe` (~200 KB) + `sqlite3.exe`
