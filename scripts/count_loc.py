import os

def count_lines(directory="."):
    total_files = 0
    total_lines = 0
    total_code = 0
    total_comments = 0
    total_blank = 0

    print("=" * 60)
    print(f"{'Module Path':<35} | {'Files':<6} | {'Lines':<8}")
    print("=" * 60)

    for root, dirs, files in os.walk(directory):
        if any(ignored in root for ignored in [".git", "__pycache__", ".venv", "build", "dist"]):
            continue
        
        py_files = [f for f in files if f.endswith(".py")]
        if not py_files:
            continue
        
        module_lines = 0
        for file in py_files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    module_lines += len(lines)
                    for line in lines:
                        stripped = line.strip()
                        if not stripped:
                            total_blank += 1
                        elif stripped.startswith("#"):
                            total_comments += 1
                        else:
                            total_code += 1
            except Exception as e:
                pass
        
        total_files += len(py_files)
        total_lines += module_lines
        rel_root = os.path.relpath(root, directory)
        print(f"{rel_root:<35} | {len(py_files):<6} | {module_lines:<8}")

    print("=" * 60)
    print(f"Total Python Files : {total_files}")
    print(f"Total Lines of Code: {total_lines}")
    print(f"  - Executable Code : {total_code}")
    print(f"  - Comments        : {total_comments}")
    print(f"  - Blank Lines     : {total_blank}")
    print("=" * 60)

if __name__ == "__main__":
    count_lines(".")
