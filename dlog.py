import argparse
from commands import export, note, start, stats, stop
import storage

def main():
    parser = argparse.ArgumentParser(prog='dlog',
                                 description='CLI tool to track your dev sessions')

    subparser = parser.add_subparsers()

    start_parser = subparser.add_parser('start')
    start_parser.add_argument('project')
    start_parser.set_defaults(func=start.run)

    stop_parser = subparser.add_parser('stop')
    stop_parser.set_defaults(func=stop.run)

    export_parser = subparser.add_parser('export')
    export_parser.set_defaults(func=export.run)

    note_parser = subparser.add_parser('note')
    note_parser.add_argument('text')
    note_parser.set_defaults(func=note.run)

    stats_parser = subparser.add_parser('stats')
    stats_parser.set_defaults(func=stats.run)

    clear_parser = subparser.add_parser('clear')
    clear_parser.set_defaults(func=storage.clear)

    args = parser.parse_args()

    args.func(args)