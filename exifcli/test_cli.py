import unittest
import tempfile
import os
import shutil
from exif import Image

from cli import add_exif


class TestUtils(unittest.TestCase):

  def test_add_exif_date(self):
    datadir = os.path.join(os.path.dirname(__file__), "../dataset")
    with tempfile.TemporaryDirectory() as tempdir:

      test_files = []

      for filename in os.listdir(datadir):
        src = os.path.join(datadir, filename)
        dst = os.path.join(tempdir, filename)

        # copy only files
        if os.path.isfile(src):
            shutil.copy(src, dst)
            test_files.append(dst)

      # Add EXIF attributes
      add_exif(test_files, date="1985", override=True)

      # Read files
      for test_file in test_files:
        my_image = Image(test_file)
        self.assertEqual(my_image.datetime_original, "1985:01:01 12:00:00+00:00")

# TODO Add missing tests:
# * [ ] Test with override=False
# * [ ] Test add_exif location
# * [ ] Test unique


if __name__ == '__main__':
    unittest.main()

