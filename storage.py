import json
from pathlib import Path

session_file = Path('data/sessions.json')
def load():    
    try:
        with session_file.open() as f:
            return json.load(f)
    except(json.JSONDecodeError, FileNotFoundError):
        return []
    
def save(data):
    session_file.write_text(json.dumps(data, indent=4))

def clear(args):
    choice = input("▶ Do you want to clear all data?: ")
    if choice == "y":
        new_data = []
        for s in load():
            print(f"▶ {s["project"]} - Data cleared")
            session_file.write_text(json.dumps(new_data, indent=4))
            return
        print("▶ No session found")
    else:
        return