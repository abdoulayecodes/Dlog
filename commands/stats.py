import storage

def run(args):
    session = storage.load()
    for s in session:
        if not s["end"] == None:
            print(f"▶ Project: {s['project']}\n▶ Notes taken:\n{s['notes']}\n▶ Time spent: work in progress")
            return
    print("▶ A session is running")
    
    