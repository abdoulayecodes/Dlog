import argparse
from commands import export, note, start, stats, stop

parser = argparse.ArgumentParser(prog='dlg')
subparsers = parser.add_subparsers()

start_parser = subparsers.add_parser('start')
start_parser.add_argument('project')
start_parser.set_defaults(func=start.run)

stop_parser = subparsers.add_parser('stop')
stop_parser.set_defaults(func=stop.run)

export_parser = subparsers.add_parser('export')
export_parser.set_defaults(func=export.run)

note_parser = subparsers.add_parser('note')
note_parser.add_argument('text')
note_parser.set_defaults(func=note.run)

stats_parser = subparsers.add_parser('stats')
stats_parser.set_defaults(func=stats.run)

args = parser.parse_args()