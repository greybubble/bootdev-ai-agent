from functions.get_files_info import get_files_info
from functions.write_file_content import write_file
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from config import WORKING_DIRECTORY

from google import genai
from google.genai import types



def call_function(function_call_part, verbose=False):
    wdir = WORKING_DIRECTORY
    fname = function_call_part.name
    fargs = function_call_part.args.copy()
    fargs["working_directory"] = wdir

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Calling function: {function_call_part.name}")

    func_output = None

    match (fname):
        case ("get_files_info"):
            func_output = get_files_info(**fargs)
        case ("write_file"):
            func_output = write_file(**fargs)
        case ("get_file_content"):
            func_output = get_file_content(**fargs)
        case ("run_python_file"):
            func_output = run_python_file(**fargs)
        case _:
            return types.Content(
                role="tool",
                parts=[
                types.Part.from_function_response(
                    name=fname,
                    response={"error": f"Unknown function: {fname}"},
                    )
                ],
            )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=fname,
                response={"result": func_output}
            )
        ]
    )