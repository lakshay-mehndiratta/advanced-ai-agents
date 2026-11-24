from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from tools import TOOLS, FUNCTION_NAME_TO_FUNCTION_MAP

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

messages = []

messages.append(
    {
        "role" : "system",
        "content" : "Always respond within 100 words"
    }
)

while True:
    user_input = input("Lakshay: ")

    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    messages.append(
        {
            "role" : "user",
            "content" : user_input
        }
    )

    # 1st call to LLM
    LLM_response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = messages,
        tools = TOOLS
    )

    msg = LLM_response.choices[0].message

    if msg.tool_calls: # The first call to LLM returned a tool_call, i.e. it asked to run the tools
        messages.append(msg) # Append the LLM's response to history

        for tool_call in msg.tool_calls:
            function_name = tool_call.function.name # Extract the function's name from every tool call
            function_arguments = json.loads(tool_call.function.arguments or "{}") # Extract the stringified json from tool call, then convert it to a dictionary using json.loads()

            fn = FUNCTION_NAME_TO_FUNCTION_MAP[function_name] # obtain the actual function from function_name using the map
            result = fn(**function_arguments)

            messages.append(
                {
                    "role" : "tool",
                    "tool_call_id" : tool_call.id,
                    "content" : str(result)
                }
            )

        # 2nd call to LLM API to get the final response after the tool has been executed
        LLM_response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = messages
        )

        msg = LLM_response.choices[0].message # Update the msg object after the LLM responses are appended to history

    messages.append(
        {
            "role" : "assistant",
            "content" : msg.content
        }
    )

    print("Assistant: " + msg.content) # Response from the LLM model : qwen3:4b