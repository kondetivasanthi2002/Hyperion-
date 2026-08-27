import os
import sys
import subprocess

def run_cmd(cmd, cwd="."):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if res.returncode != 0:
        print(f"Error executing command: {cmd}\nSTDERR: {res.stderr}")
    return res.stdout

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("Generator script initialized.")
