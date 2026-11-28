#standard library imports
import os

# Third - party imports
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Local module imports
from tools import TOOLS, get_curr_time, run_tool
from Utilities.utilities import log

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

messages = []

messages.append(
    {
        "role" : "system",
        "content" : f"You are a helpful AI assistant. Current date and time: {get_curr_time()}. Always respond within 100 words"
    }
)

max_steps = 10 # Maximum number of steps allowed in a single response from the LLM. This is to prevent infinite loops and excessive tool calls.

while True:
    user_input = input("😎 Lakshay: ")

    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    messages.append(
        {
            "role" : "user",
            "content" : user_input
        }
    )

    for step in range(max_steps): # Limit the number of steps to prevent infinite loops
        LLM_response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = messages,
            tools = TOOLS
        )
    
        msg = LLM_response.choices[0].message

        if not msg.tool_calls: # If the LLM response does not contain any tool calls, break the loop and return the response to the user
            break

        log(f"Step {step + 1}: model requested {len(msg.tool_calls)} tool call(s).")

        messages.append(msg) # Append the LLM's response to history

        # Process each tool call in the LLM's response
        for tool_call in msg.tool_calls:
            result = run_tool(tool_call)
            messages.append(
                {
                    "role" : "tool",
                    "tool_call_id" : tool_call.id,
                    "content" : str(result)
                }
            )

    else:
        # Ran out of steps, The model never gave the final response
        fallback = "Sorry, I couldn't finish this within the allowed number of steps. Please try again."
        messages.append(
            {
                "role" : "assistant",
                "content" : fallback
            }
        )
        print("🤖 Assistant: " + fallback)
        continue

    messages.append(
        {
            "role" : "assistant",
            "content" : msg.content
        }
    )

    print("🤖 Assistant: " + (msg.content or "")) # Response from the LLM model : qwen3:4b