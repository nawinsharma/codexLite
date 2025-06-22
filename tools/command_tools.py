import subprocess
import os
import signal

# Global variables for process management
running_processes = []

def run_command(cmd, timeout=60):
    """Run command with timeout to prevent hanging"""
    try:
        # Handle cd commands specially
        if cmd.strip().startswith('cd '):
            path = cmd.strip()[3:].strip()
            try:
                os.chdir(path)
                return f"Changed directory to: {os.getcwd()}"
            except Exception as e:
                return f"Failed to change directory: {e}"
        
        # Check for server commands that should use run_server instead
        server_commands = ['npm start', 'npm run dev', 'yarn start', 'yarn dev', 
                          'flask run', 'python -m flask run', 'python app.py',
                          'node server.js', 'nodemon', 'serve', 'http-server']
        
        if any(server_cmd in cmd.lower() for server_cmd in server_commands):
            return f"⚠️ This looks like a server command. Use 'run_server' tool instead of 'run_command' for: {cmd}"
        
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout,
            cwd=os.getcwd()
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout} seconds: {cmd}"
    except Exception as e:
        return f"Command failed: {e}"

def run_server(cmd):
    """Start server in background with process tracking"""
    try:
        process = subprocess.Popen(
            cmd, 
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        running_processes.append(process)
        return f"Server started (PID: {process.pid}): {cmd}"
    except Exception as e:
        return f"Error starting server: {e}"

def stop_servers():
    """Stop all running servers"""
    stopped = 0
    for process in running_processes:
        try:
            process.terminate()
            process.wait(timeout=5)
            stopped += 1
        except:
            try:
                process.kill()
                stopped += 1
            except:
                pass
    running_processes.clear()
    return f"Stopped {stopped} running processes" 