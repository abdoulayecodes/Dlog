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
            print(f"▶ Time elapsed: {time_delta}")
            storage.save(session)
            return
    print("▶ No session found")
           
    
    