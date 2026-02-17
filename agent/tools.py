from tools.file_tools import create_file
from tools.browser_tools import open_browser
from tools.screen_tools import capture_screen
from tools.web_tools import search_web

TOOLS = {
    "create_file": lambda a: create_file(a["filename"], a["content"]),
    "open_browser": lambda a: open_browser(a["url"]),
    "capture_screen": lambda a: capture_screen(),
    "search_web": lambda a: print(search_web(a["query"]))
}

def run_tool(cmd):
    tool = cmd.get("tool")
    args = cmd.get("args", {})

    if tool in TOOLS:
        TOOLS[tool](args)
    else:
        print("🤖", cmd.get("message"))

