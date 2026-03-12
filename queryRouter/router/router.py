from ..config import ConfigLoader
from ..models import ParsedQuery

class Router:
    def __init__(self):
        self.loader = ConfigLoader()

    def get_destination(self, parsed: ParsedQuery) -> str:
        data = self.loader.load()
        shortcuts = data.get("shortcuts", {})
        default = data.get("default_engine", "https://www.google.com/search?q=")
        current_port = data.get("port", 9191)

        # 1. System Shortcuts (Always dynamic)
        if parsed.command in ["qr", "home", "dash"]:
            return f"http://127.0.0.1:{current_port}/"

        # 2. Search for custom shortcuts/aliases
        target_conf = None
        for key, conf in shortcuts.items():
            aliases = [k.strip().lower() for k in str(key).split(",")]
            if parsed.command in aliases:
                target_conf = conf
                break

        if target_conf:
            if parsed.query and isinstance(target_conf, dict) and "search" in target_conf:
                return target_conf["search"].replace("{query}", parsed.query)
            
            if isinstance(target_conf, dict):
                return target_conf.get("url", f"{default}{parsed.command}")
            
            if isinstance(target_conf, str):
                return target_conf

        # 3. Fallback to default engine
        sep = data.get("separator", ":")
        full_query = f"{parsed.command}{sep} {parsed.query}" if parsed.query else parsed.command
        return f"{default}{full_query}"