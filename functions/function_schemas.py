from google import genai
from google.genai import types



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Outputs the contents of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file for which we want to output the contents, relative to the working directory.",
            ),
            
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script contained within a specified python file using the python interpreter, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file containing the python script we want to run, relative to the working directory. ",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="A list of additional arguments needed to run the python script we want to run. If not provided, then the python script will attempt to run without additional arguments.",
            ),
        },
    ),
)
schema_write_file_content = types.FunctionDeclaration(
    name="write_file",
    description="Writes new information to a specified file, constrained to the working directory. Any information in the file before the write action is no longer there.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file we want write in, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we want to write to a file.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file_content
    ]
)

