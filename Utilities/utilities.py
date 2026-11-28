import os

START_ANSI_CODE = "\033[90m"
END_ANSI_CODE = "\033[0m"

def log(text):
    if os.getenv("DEBUG") == "True":
        print(f"  {START_ANSI_CODE}{text}{END_ANSI_CODE}")