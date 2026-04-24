import storage

def run(args):
    sessions = storage.load()
    for s in sessions:
        print(f"▶ Project - {s['project']}")
        for n in s['notes']:
            print(f"    - {n}")
        if not sessions:
            print("▶ No sessions found")
            return
