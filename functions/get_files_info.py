import os

def get_files_info(working_directory, directory="."):
    wd_path = os.path.abspath(working_directory)
    target_path = os.path.join(working_directory, directory)
    target_path = os.path.abspath(target_path)
 
    title = ""

    if directory == ".":
        title = f"Result for current directory:"
    else:
        title = f"Result for '{directory}' directory:"

    if not target_path.startswith(wd_path):
        return '\n'.join([title, f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'])
    
    if not os.path.isdir(target_path):
        return '\n'.join([title, f'    Error: "{directory}" is not a directory'])
    
    contents = os.listdir(target_path)
    result = [title]

    for file in contents:
        if file == "__pycache__":
            continue
        path_to_file = os.path.join(target_path, file)
        result.append(f" - {file}: file_size={os.path.getsize(path_to_file)} bytes, is_dir={os.path.isdir(path_to_file)}")

    return "\n".join(result)