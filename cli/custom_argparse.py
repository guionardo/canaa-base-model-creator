import argparse
import sys as _sys


class CustomArgumentParser(argparse.ArgumentParser):

    def exit(self, status, message):
        if message:
            self._print_message(message, _sys.stderr)
        if self.testing:
            raise Exception('Exiting with status {0}'.format(status))
        else:
            _sys.exit(status)
