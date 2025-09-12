import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


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
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)


    print("Hello from bootdev-ai-agent!")
    print("Let's chat.")

    if verbose:
        print(f"User prompt: {query}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(response.text)


if __name__ == "__main__":
    main()
