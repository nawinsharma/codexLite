import os
import glob
from pathlib import Path

def create_folder(path):
    """Create folder with better error handling"""
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return f"Folder created: {os.path.abspath(path)}"
    except Exception as e:
        return f"Error creating folder: {e}"

def write_file(data):
    """Write file with backup and validation"""
    try:
        if isinstance(data, dict):
            path = data.get("path")
            content = data.get("content")
            if not path or content is None:
                return "Invalid input: 'path' and 'content' are required."
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            # Backup existing file if it exists
            if os.path.exists(path):
                backup_path = f"{path}.backup"
                os.rename(path, backup_path)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"File written: {os.path.abspath(path)}"
        else:
            return "Input must be a dictionary with 'path' and 'content'."
    except Exception as e:
        return f"Error writing file: {e}"

def read_file(path):
    """Read file contents"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"File content ({path}):\n{content}"
    except Exception as e:
        return f"Error reading file: {e}"

def list_files(path="."):
    """List files and directories with details"""
    try:
        items = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                items.append(f"📁 {item}/")
            else:
                size = os.path.getsize(item_path)
                items.append(f"📄 {item} ({size} bytes)")
        return f"Contents of {os.path.abspath(path)}:\n" + "\n".join(items)
    except Exception as e:
        return f"Error listing files: {e}"

def find_files(pattern, path="."):
    """Find files matching pattern"""
    try:
        matches = glob.glob(os.path.join(path, pattern), recursive=True)
        if matches:
            return f"Found files matching '{pattern}':\n" + "\n".join(matches)
        else:
            return f"No files found matching '{pattern}'"
    except Exception as e:
        return f"Error finding files: {e}" 