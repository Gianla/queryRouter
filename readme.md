# 🚀 QueryRouter

**QueryRouter** is a lightweight, modular local tool that transforms your browser's address bar into a powerful command center. Powered by a local FastAPI server, you can define custom search shortcuts (e.g., `yt:music`, `gh:fastapi`) and manage them via a sleek web dashboard, effortlessly bypassing the search engine restrictions of modern browsers.

------

## ✨ Features

- **⚡ Hot-Reload**: Edit the `config.yaml` file and changes are applied instantly—no server restart required.
- **🌐 Cross-Browser**: Works seamlessly across Brave, Chrome, Safari, Firefox, and Edge.
- **🎨 Web Dashboard**: A modern UI to manage your shortcuts (Add, Edit, Delete) without touching code.
- **🛠️ Clean Architecture**: Modular structure divided into Parser, Router, and Models for maximum extensibility.
- **🖥️ Integrated CLI**: Manage the tool with simple commands via the built-in command-line interface (e.g., `qr start`).
- **🥷 Background Mode**: Support for invisible startup execution on Windows (via VBS script) and macOS (via native LaunchAgents).

------

## 📂 Project Structure


```plaintext
.
├── config.yaml          # Your shortcut database & settings
├── setup.py             # Python package configuration
├── queryRouter/         # Application core
│   ├── config/          # Dynamic YAML config loader
│   ├── models/          # Pydantic data schemas
│   ├── parser/          # Query extraction logic
│   ├── router/          # Redirection logic
│   ├── cli.py           # Command-line interface
│   └── server.py        # FastAPI server & Web Dashboard
└── run_router.vbs       # Invisible launcher (Windows only)
```

------

## 🚀 Installation

1. Ensure you have **Python 3.8+** installed on your system.

   ```
   python --version
   ```

2. Clone or download this repository.

   ```bash
   git clone https://github.com/your-username/queryRouter.git
   cd queryRouter
   ```

3. Open your terminal in the project directory and install it in editable mode:

   ```bash
   pip install -e .
   ```

   *Note: If you see a "Warning: script not on PATH," add the indicated directory to your System Environment Variables.*

------

## ⚙️ Configuration (`config.yaml`)

Customize your shortcuts and server settings. The app reloads these automatically.

```yaml
port: 9191
separator: ":"  # Change to " " to use space-based search
default_engine: "https://www.google.com/search?q="

shortcuts:
  yt, tube:
    url: "https://www.youtube.com/"
    search: "https://www.youtube.com/results?search_query={query}"
  gh:
    url: "https://github.com/"
    search: "https://github.com/search?q={query}"
```

------

## 💻 CLI Usage

The tool can be invoked from anywhere in your terminal using the `qr` command.

- **Start the server manually**:

  ```bash
  qr start
  ```

- **Install as a background service (macOS only)**:

  ```bash
  qr install
  ```

- **Remove the background service (macOS only)**:

  ```bash
  qr uninstall
  ```

------

## 🌐 Browser Configuration

### Brave / Chrome / Edge

1. Go to browser Settings and look for **"Search engine"** or **"Site search"**.
2. Add a new search engine:
   - **Search engine**: `QueryRouter`
   - **Shortcut**: `@q` (or set as Default)
   - **URL with %s**: `http://127.0.0.1:9191/search?q=%s`

### Safari (macOS)

Install the free **Keyword Search** extension and set the Search URL to: `http://127.0.0.1:9191/search?q={query}`



### 🏠 Dashboard Access

Access the management UI instantly by typing any of these magic shortcuts in your browser:

- `qr`
- `home`
- `dash`

------

## 🛠️ Built With

- **[FastAPI](https://fastapi.tiangolo.com/)**: For lightning-fast HTTP redirects.
- **[Typer](https://typer.tiangolo.com/)**: For the modern CLI experience.
- **[TailwindCSS](https://tailwindcss.com/)**: For the sleek dashboard UI.
- **[Pydantic](https://www.google.com/search?q=https://docs.pydantic.dev/)**: For robust data validation.