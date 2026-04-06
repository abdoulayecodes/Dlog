import storage

def run(args):
    session = storage.load()
    for s in session:
        if s["end"] == None:
            s["notes"].append(args.text)
            print(f"▶ {s['project']} - note added")
            storage.save(session)
            return
    print("▶ No session found")
        
    