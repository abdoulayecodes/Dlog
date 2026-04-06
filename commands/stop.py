import storage
from datetime import datetime

def run(args):
    session = storage.load()
    for s in session:
        if s["end"] == None:

            s["end"] = str(datetime.now())
            print(f"▶ {s["project"]} - session stopped")

            start = datetime.strptime(s["start"], "%Y-%m-%d %H:%M:%S.%f")
            end = datetime.strptime(s["end"], "%Y-%m-%d %H:%M:%S.%f")
            time_delta = end - start
            total_seconds = int(time_delta.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

            if hours > 0:
                print(f"▶ Time elapsed: {hours}h {minutes}m {seconds}s")
            else:
                print(f"▶ Time elapsed: {minutes}m {seconds}s")
            
            storage.save(session)
            return
    print("▶ No session found")
           
    
    