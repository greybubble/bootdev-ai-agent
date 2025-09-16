import os

def write_file(working_directory, file_path, content):
    wd_path = os.path.abspath(working_directory)
    target_path = os.path.join(working_directory, file_path)
    target_path = os.path.abspath(target_path)
 
    if not target_path.startswith(wd_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    path_to_file = target_path[:target_path.rfind("/")]

    if not os.path.exists(path_to_file):
        print(f"path does not exist: {path_to_file}")
        try:
            os.makedirs(path_to_file)
            print(f"file path created: {path_to_file}")
        except Exception as e:
            return f"Error: unable to create file path: {e}"
        
    if os.path.exists(target_path) and os.path.isdir(target_path):
        return f"Error: {file_path} is a directory, not a file"

    try:
        with open(target_path, "w") as f:
            f.write(content)
            f.close()
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Could not open or write to file: {e}"
    
    