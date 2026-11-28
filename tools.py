import os
from datetime import datetime
import requests
from tavily import TavilyClient

def get_curr_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_city_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url, timeout=10)
    response.raise_for_status() # This will raise HTTPError if something goes wrong
    return response.text

def web_search(query):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = client.search(
        query = query,
        max_results = 5,
        search_depth = "basic"
    )

    response.raise_for_status() 

    results = []

    for result in response.get("results", []):
        results.append({
            "title" : result.get("title"),
            "url" : result.get("url"),
            "content" : result.get("content"),
        })

    return results


# TOOLS = [{}, {}, {}]
TOOLS = [
    {
        "type" : "function",
        "function" : {
            "name" : "get_curr_time",
            "description" : "Returns the current date and time as a formatted string.",
            "parameters" : {"type" : "object", "properties" : {}},
        }
    },
    {
        "type" :"function",
        "function" : {
            "name" : "get_city_weather",
            "description" : "Returns the current weather for a given city.",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "city" : {
                        "type" : "string",
                        "description" : "The name of the city to get the weather for."
                    }
                },
                "required" : ["city"],
            }
        }
    },
    {
        "type" : "function",
        "function" : {
            "name" : "web_search",
            "description" : "Searches the internet for information about a given query and returns relevant web pages with their titles, URLs, and content.",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query" : {
                        "type" : "string",
                        "description" : "The search query to look up on the internet."
                    }
                },
                "required" : ["query"],
            }
        }
    }
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_curr_time" : get_curr_time,
    "get_city_weather" : get_city_weather,
    "web_search" : web_search,
}