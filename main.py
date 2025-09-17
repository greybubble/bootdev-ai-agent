import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.function_schemas import *
from functions.call_function import call_function

import prompts

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
system_prompt = prompts.SYSTEM_PROMPT

def main():
    verbose = False
    if len(sys.argv) < 2:
        print("Prompt was not provided")
        exit(code=1)
    if len(sys.argv) > 2 and "--verbose" in sys.argv:
        verbose = True

    query = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=query)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
            )
    )

    if verbose:
        print(f"User prompt: {query}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print("Text Response:")
    print(response.text)
    print("---------------------")

    print("Function Response:")
    if response.function_calls:
        for func in response.function_calls:
            result = call_function(func, verbose)
            if not result.parts[0].function_response.response:
                raise Exception("Error: Did not receive response from function call.")
            print(f"-> {result.parts[0].function_response.response}")

    else:
        print("none")

if __name__ == "__main__":
    main()
