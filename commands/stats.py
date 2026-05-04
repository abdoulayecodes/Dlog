
import storage
from datetime import datetime


def format_duration(seconds):
    minutes = int(seconds // 60)
    hours = minutes // 60
    minutes = minutes % 60

    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def run(args):
    sessions = storage.load()

    if not sessions:
        return

    
    total_seconds = 0
    parsed_sessions = []

    for s in sessions:
        start = datetime.fromisoformat(s["start"])
        end = datetime.fromisoformat(s["end"])
        duration = (end - start).total_seconds()

        total_seconds += duration

        parsed_sessions.append({
            "project": s["project"],
            "start": start,
            "end": end,
            "duration": duration,
            "notes": s["notes"]
        })

    # global stats
    nb_sessions = len(parsed_sessions)
    avg_seconds = total_seconds / nb_sessions

    project_name = parsed_sessions[0]["project"]  

    with open(r"output\stats.txt", "w") as f:
        f.write(f"""=== dlog stats ===
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Project: {project_name}
Sessions: {nb_sessions}
Total time: {format_duration(total_seconds)}
Average session: {format_duration(avg_seconds)}

""")

        # sessions details
        for i, s in enumerate(parsed_sessions, start=1):
            f.write(f"""--- Session {i} ---
Start: {s["start"].strftime("%Y-%m-%d %H:%M")}
End:   {s["end"].strftime("%Y-%m-%d %H:%M")}
Duration: {format_duration(s["duration"])}
Notes:
""")

            if s["notes"]:
                for note in s["notes"]:
                    f.write(f"  - {note}\n")
            else:
                f.write("  (no notes)\n")

            f.write("\n")

    print("▶ stats.txt generated")