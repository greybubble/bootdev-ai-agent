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
 
    max_iterations = 20
    iterations = 0    
    no_response = True

    while iterations < max_iterations and no_response:
        iterations += 1

        #print(f"Messages: {messages}")
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                    
                    )
            )

            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.function_calls:
                func_call_responses = []
                for func in response.function_calls:
                    result = call_function(func, verbose)
                    if not result.parts[0].function_response.response:
                        raise Exception("Error: Did not receive response from function call.")
                    if verbose:
                        print(f"-> {result.parts[0].function_response.response}")
                        print("---------------------")
                    
                    func_call_responses.append(result.parts[0])
                    
                messages.append(types.Content(role="user", parts=func_call_responses))

            else:

                if response.text != None:
                    no_response = False
                    
            if not no_response:
                if verbose:
                    print(f"User prompt: {query}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                
                print("Text Response:")
                print(response.text)
        except Exception as e:
            print(f"Error during query iteration {iterations}: {e}")
            return f"Error during query iteration {iterations}: {e}"


if __name__ == "__main__":
    main()
