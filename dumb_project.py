import os

# Set the folders/files you want to IGNORE
IGNORE_DIRS = {'.git', '__pycache__', 'venv', 'env', '.idea', '.vscode'}
IGNORE_FILES = {'.DS_Store', 'dump_project.py', 'document.txt', 'poetry.lock'}

def print_project_structure(startpath):
    print(f"--- PROJECT STRUCTURE: {startpath} ---")
    for root, dirs, files in os.walk(startpath):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f not in IGNORE_FILES and f.endswith(('.py', '.md', '.txt')):
                print(f'{subindent}{f}')

def print_file_contents(startpath):
    print("\n\n--- FILE CONTENTS ---")
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file in IGNORE_FILES or not file.endswith(('.py', '.md')): 
                continue
                
            path = os.path.join(root, file)
            print(f"\n# ==========================================")
            print(f"# FILE: {path}")
            print(f"# ==========================================")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    print(f.read())
            except Exception as e:
                print(f"[Error reading file: {e}]")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print_project_structure(current_dir)
    print_file_contents(current_dir)