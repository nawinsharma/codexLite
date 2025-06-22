import os
import socket

def get_current_directory():
    """Get current working directory"""
    return f"Current directory: {os.getcwd()}"

def check_port(port):
    """Check if port is in use"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('localhost', int(port)))
            if result == 0:
                return f"Port {port} is in use"
            else:
                return f"Port {port} is available"
    except Exception as e:
        return f"Error checking port: {e}" 