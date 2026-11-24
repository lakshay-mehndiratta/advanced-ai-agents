from datetime import datetime

def get_curr_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# TOOLS = [{}, {}, {}]
TOOLS = [
    {
        "type" : "function",
        "function" : {
            "name" : "get_curr_time",
            "description" : "Returns the current date and time as a formatted string.",
            "parameters" : {"type" : "object", "properties" : {}},
        }
    }
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_curr_time" : get_curr_time,
}