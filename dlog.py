import argparse
from commands import note, start, stats, stop, check
import storage


def main():
    parser = argparse.ArgumentParser(
        prog='dlog',
        description='CLI tool to track your dev sessions')

    subparser = parser.add_subparsers()

    # 'start' command requires a project name
    start_parser = subparser.add_parser('start') 
    start_parser.add_argument('project') 
    start_parser.set_defaults(func=start.run) 

    # 'stop' command ends current session
    stop_parser = subparser.add_parser('stop')
    stop_parser.set_defaults(func=stop.run)

    # 'note' command requires a text which will be put in sessions.json
    note_parser = subparser.add_parser('note')
    note_parser.add_argument('text')
    note_parser.set_defaults(func=note.run)

    # 'stats' command shows the selected project's stats
    stats_parser = subparser.add_parser('stats')
    # stats_parser.add_argument('project')
    stats_parser.set_defaults(func=stats.run)

    # 'clear' command wipes sessions.json
    clear_parser = subparser.add_parser('clear')
    clear_parser.set_defaults(func=storage.clear)

    check_parser = subparser.add_parser('check')
    check_parser.set_defaults(func=check.run)

    args = parser.parse_args()

    if not hasattr(args, 'func'):
        parser.print_help()
        return
    args.func(args)