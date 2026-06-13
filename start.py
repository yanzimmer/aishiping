from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 4173


def candidate_node_roots() -> list[Path]:
    home = Path.home()
    candidates = [
        home / "Documents" / "Codex" / "2026-05-08" / "usb-opencv" / "frontend" / ".tools" / "node-v24.14.0-win-x64"
    ]

    codex_dir = home / "Documents" / "Codex"
    if codex_dir.exists():
        candidates.extend(sorted(codex_dir.glob("**/.tools/node-*-win-x64")))

    unique: list[Path] = []
    seen: set[str] = set()
    for path in candidates:
        resolved = str(path)
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start the Vue 3 Vite development server.")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Bind host, default: {DEFAULT_HOST}")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Bind port, default: {DEFAULT_PORT}")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    return parser.parse_args()


def ensure_project_files() -> None:
    required = [
        ROOT / "package.json",
        ROOT / "vite.config.js",
        ROOT / "index.html",
        ROOT / "src" / "main.js",
        ROOT / "src" / "App.vue"
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required project files:\n" + "\n".join(missing))


def find_npm_command() -> str | None:
    for command in ("npm.cmd", "npm"):
        path = shutil.which(command)
        if path:
            return path

    for root in candidate_node_roots():
        npm_cmd = root / "npm.cmd"
        if npm_cmd.exists():
            return str(npm_cmd)
    return None


def open_browser(url: str) -> None:
    time.sleep(1.2)
    webbrowser.open(url)


def build_runtime_env(npm_command: str) -> dict[str, str]:
    env = dict(**__import__("os").environ)
    npm_path = Path(npm_command)
    node_root = npm_path.parent
    node_exe = node_root / "node.exe"

    path_entries = [str(node_root), env.get("PATH", "")]
    env["PATH"] = ";".join(entry for entry in path_entries if entry)

    if node_exe.exists():
        env["NODE"] = str(node_exe)

    return env


def main() -> int:
    args = parse_args()

    try:
        ensure_project_files()
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    npm_command = find_npm_command()
    if not npm_command:
        print("Error: npm was not found in PATH.", file=sys.stderr)
        print("Install Node.js first, then run:", file=sys.stderr)
        print("  npm install", file=sys.stderr)
        print("  python start.py", file=sys.stderr)
        return 1

    url = f"http://{args.host}:{args.port}/"
    command = [npm_command, "run", "dev", "--", "--host", args.host, "--port", str(args.port)]
    env = build_runtime_env(npm_command)

    print(f"Project: {ROOT}")
    print(f"Preview: {url}")
    print(f"Command: {' '.join(command)}")
    print("Press Ctrl+C to stop.")

    if not args.no_browser:
        threading.Thread(target=open_browser, args=(url,), daemon=True).start()

    try:
        return subprocess.call(command, cwd=ROOT, env=env)
    except KeyboardInterrupt:
        print("\nServer stopped.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
