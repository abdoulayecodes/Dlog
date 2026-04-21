import storage
from datetime import datetime
from collections import defaultdict


def run(args):

    sessions = storage.load()
    
    projects = defaultdict(list)
    for s in sessions:
        projects[s["project"]].append(s)
    
    print(projects)