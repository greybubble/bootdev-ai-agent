import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    wd_path = os.path.abspath(working_directory)
    target_path = os.path.join(working_directory, file_path)
    target_path = os.path.abspath(target_path)
 
    if not target_path.startswith(wd_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    
    if target_path[target_path.rfind('.'):] != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        arg_list = ["python", target_path]
        arg_list.extend(args)
        result = subprocess.run(arg_list, capture_output=True, timeout=30, cwd=wd_path)
        exit_code = result.returncode

        output = []

        if result.stdout:
            output.append(f"STDOUT: {result.stdout.decode()}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr.decode()}")
        
        if exit_code != 0:
            output.append(f"\nProcess exited with code {exit_code}")

        if not output:
            f"No output produced."

        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
