import argparse
import os
from pathlib import Path
import platform
import tempfile
import sys
import re
from exif import Image
from .cli import add_exif


def main():
  parser = argparse.ArgumentParser(prog='exif-cli')
  subparsers = parser.add_subparsers(title='subcommands',
                                     description='valid subcommands',
                                     help='additional help')
  import_parser = subparsers.add_parser('add')
  import_parser.add_argument('--date', default=None, nargs="+", help="original date")
  import_parser.add_argument('--date-unique', default=False, action='store_true', help="increment dates to be unique")
  import_parser.add_argument('--location', default=".", help="GPS coordinates")
  import_parser.add_argument('--override', default=False, help="override files")
  import_parser.add_argument('files', action='append', help="pictures to edit")
  args = parser.parse_args()

  # TODO test which subparser was use
  add_exif(args.files, date=args.date, date_unique=args.date_unique, location=args.location, override=args.override)

if __name__ == '__main__':
    main()
