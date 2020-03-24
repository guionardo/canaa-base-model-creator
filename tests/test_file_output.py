import os
import unittest

from cli.create_files.file_output import write_file


class TestFileOutput(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join('docs', 'testing.py')
        self.code = """
import os
class testing:
  def __init__(self):
    print('TESTING')
"""

    def __del__(self):
        if os.path.isfile(self.filename):
            os.unlink(self.filename)

    def test_file_output(self):
        if write_file(self.filename, self.code):
            write_file(self.filename, self.code)

        self.assertTrue(os.path.isfile(self.filename))

    def test_file_output_error(self):
        self.assertFalse(write_file(os.path.join(
            'docs_error', 'testing.py'), self.code))
