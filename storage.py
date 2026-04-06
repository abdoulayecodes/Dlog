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
