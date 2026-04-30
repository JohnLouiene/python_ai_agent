import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("API key does not exist")

    client = genai.Client(api_key=api_key)
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    #Agent loop
    for _ in range(20):
        done = generate_content(client=client, messages=messages, args=args)
        if done:
            break
    else:
        print("Iteration limit reached")
        sys.exit(1)

def generate_content(client, messages, args):
    #Function to call the model
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents= messages,
            config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt

            #Set temperature based on how much you want to deviate from the system prompt"
            #temperature=0
                )
            )
    except Exception as e:
        raise RuntimeError("API did not connect") from e

    if response.usage_metadata == None:
        raise RuntimeError("Usage metadata not received")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    
    #Appending responses to act as memory loop
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    #Function call handling
    function_results = []

    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, args.verbose)

            if not function_call_result.parts:
                raise Exception("Empty parts in function call result")
            
            part = function_call_result.parts[0]

            if not part.function_response:
                raise Exception("Missing function_response on part")
            if not part.function_response.response:
                raise Exception("Missing response in function_response")
        
            function_results.append(part)

            if args.verbose:
                print(f"-> {part.function_response.response}")
    else:
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {response_token_count}")
        print(f"Response:\n{response.text}")
        #End loop if a text is returned
        return True
    
    if function_results:
        messages.append(types.Content(role="user", parts=function_results))
    
    #Continue loop if a function is called
    return False

if __name__ == "__main__":
    main()
