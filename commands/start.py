from datetime import datetime
import storage

def run(args):
    session = storage.load()
    for s in session:
        if s["end"] == None:
            print(f"▶ {s['project']} is still running")
            return
    new_session = {
        "project": args.project,
        "start": str(datetime.now()),
        "end": None,
        "notes": []
    }

    session.append(new_session)
    storage.save(session)

    print(f"▶ {args.project} - session started")