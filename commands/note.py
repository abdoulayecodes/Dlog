import storage
from datetime import datetime

def run(args):
    session = storage.load()
    for s in session:
        if s["end"] == None:
            s["notes"].append(args.text)
            storage.save(session)
            print(f"▶ {s['project']} - notes saved")
            return
    print("▶ No session found")
    