# 🚀 QueryRouter

**QueryRouter** is a lightweight, modular local tool that transforms your browser's address bar into a powerful command center. Powered by a local FastAPI server, you can define custom search shortcuts (e.g., `yt:music`, `gh:fastapi`) and manage them via a sleek web dashboard, effortlessly bypassing the search engine restrictions of modern browsers.

------

## ✨ Features

- **⚡ Hot-Reload**: Edit the `config.yaml` file and changes are applied instantly.
- **🌐 Cross-Browser**: Works across Brave, Chrome, Safari, Firefox, and Edge.
- **🎨 Web Dashboard**: A modern UI to manage your shortcuts without touching code.
- **🛠️ Clean Architecture**: Modular structure divided into Parser, Router, and Models.
- **🖥️ Integrated CLI**: Manage the tool with simple `qr` commands.
- **🥷 Background Mode**: Support for invisible startup execution on Windows (VBS) and macOS (LaunchAgents).

------

## 🚀 Installation

1. **Clone the repository**:

   Bash

   ```
   git clone https://github.com/comiago/queryRouter.git
   cd queryRouter
   ```

2. **Install in editable mode**:

   Bash

   ```
   pip install -e .
   ```

### ⚠️ Important: Path Configuration (Windows)

If you see a warning stating `The script qr.exe is installed in [Path] which is not on PATH`, you **must** add that folder to your System Environment Variables for the `qr` command to work:

1. Copy the path shown in the warning.
2. Search for "Edit the system environment variables" in Windows.
3. Click **Environment Variables** > Select **Path** > **Edit** > **New**.
4. Paste the path and click **OK**.

------

## ⚙️ Configuration (`config.yaml`)

The app reloads automatically whenever you save this file.

YAML

```
port: 9191
separator: ":"  # Syntax style (e.g., "yt:query")
default_engine: "https://www.google.com/search?q="

shortcuts:
  yt, tube:
    url: "https://www.youtube.com/"
    search: "https://www.youtube.com/results?search_query={query}"
```

------

## 💻 CLI & Background Execution

### Manual Control

- **Start server**: `qr start`
- **macOS Service**: `qr install` / `qr uninstall`

### 🪟 Windows: Run on Startup (Recommended)

To make QueryRouter start automatically and invisibly when you turn on your PC:

1. Press `Win + R`, type `shell:startup`, and press Enter.
2. **Right-click** the `run_router.vbs` file in your project folder and select **Create shortcut**.
3. **Move** that new shortcut into the Startup folder you just opened.
4. Done! QueryRouter will now run in the background every time you log in.

------

## 🌐 Browser Configuration

To activate QueryRouter, you must instruct your browser to send searches to the local server.

### Brave / Chrome / Edge

1. Go to **Settings** > **Search engine** > **Manage search engines and site search**.

2. Under **Site search**, click **Add**:

   - **Search engine**: `QueryRouter`
   - **Shortcut**: `@q`
   - **URL with %s**: `http://127.0.0.1:9191/search?q=%s`

   And set it as default search engine

### Safari (macOS)

Since Safari doesn't natively support custom engines, use this free and open-source extension:

1. Install **[Custom Search Engine](https://www.google.com/search?q=https://apps.apple.com/us/app/custom-search-engine/id1556615930)** from the Mac App Store.
2. Open the extension and go to “Default Search Engine” section and write in “Search URL `http://127.0.0.1:9191/search?q={query}`
3. Make sure the extension is enabled in *Safari -> Settings -> Extensions*.

------

## 💻 Background Execution & Autostart

Don't want to open a terminal every time? Here is how to keep QueryRouter running silently in the background.

### 🍎 macOS (LaunchAgent)

QueryRouter includes a built-in command to handle the macOS background service using `launchd`.

- **Install Service**:

  Bash

  ```
  qr install
  ```

  *This creates a `.plist` file in your `~/Library/LaunchAgents` folder so the server starts automatically when you log in.*

- **Remove Service**:

  Bash

  ```
  qr uninstall
  ```

### 🪟 Windows (Startup Folder)

1. Ensure `run_router.vbs` is in your project folder.
2. Press `Win + R`, type `shell:startup`, and press Enter.
3. **Right-click** `run_router.vbs` > **Create shortcut**.
4. **Move** that shortcut into the Startup folder.
5. The server will now run invisibly in the background on every login.

------

### 🏠 Dashboard Access

Access the management UI instantly by typing any of these "magic" shortcuts in your address bar:

`qr`, `home`, or `dash`.

------

## 🛠️ Built With

- **FastAPI** & **Typer**
- **TailwindCSS**
- **Pydantic** & **PyYAML**