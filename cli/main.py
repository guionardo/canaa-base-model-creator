import argparse
import sys
import os

from cli.process_files import process_files
from cli.arguments import Arguments

_testing_args = []


def exit(exit_code, exit_exception=None):
    if not _testing_args:
        sys.exit(exit_code)  # pragma: no cover

    if exit_exception:
        raise exit_exception


def main():
    if _testing_args:
        args = Arguments.create(_testing_args)
    else:
        args = Arguments.create()
        
    exit_code = args.validate()

    if exit_code < 2:
        if _testing_args:
            return False
        exit(exit_code)

    exit_code = int(not process_files(
        args.source,
        args.destiny,
        args.just_validate,
        args.ignore_field_errors,
        args.old_canaa_base))

    if not _testing_args:
        exit(exit_code)


if __name__ == "__main__":
    main()
