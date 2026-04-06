import storage
from datetime import datetime

def run(args):
    session = storage.load()
    
    for s in session:
        if s["end"] != None:
            start = datetime.strptime(s["start"], "%Y-%m-%d %H:%M:%S.%f")
            end = datetime.strptime(s["end"], "%Y-%m-%d %H:%M:%S.%f")
            time_delta = end - start
            total_seconds = int(time_delta.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

            if hours > 0:
                print(f"▶ Project: {s['project']}\n▶ Notes taken:\n{s['notes']}\n▶ Time spent: {hours}h {minutes}m {seconds}s\n")
            else:
                print(f"▶ Project: {s['project']}\n▶ Notes taken:\n{s['notes']}\n▶ Time spent: {minutes}m {seconds}s\n")
            
    print("▶ No session found")

    
    