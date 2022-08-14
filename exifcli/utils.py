import re
import sys
import math

# Counter when using the flag --date-unique
increment = 1

def format_date(date_prefix, unique=False):
  """
  Formats a complete date from a partial date.
  A unique date can be generated to preserve picture ordering.
  Returns a date in a format compatible with EXIF date attributes.
  """
  global increment

  # Support - and :
  date_prefix = date_prefix.replace("-", ":")

  # Expected output format
  template = "2001:01:01 12:00:00+00:00"

  # Inject the prefix inside the template
  full_date = date_prefix + template[len(date_prefix):]

  # Make it unique
  if unique:
    minutes = math.floor(increment / 60)
    seconds = increment - (60 * minutes)
    full_date = full_date[0:14] + "{:02d}".format(minutes) + ":" "{:02d}".format(seconds) + full_date[19:]
    increment += 1

  return full_date

def parse_location(location_raw):
  """
  Extracts the GPS coordinates from a Google Maps URL or from a substring of the URL.
  Returns the 4 fields required in EXIF attributes.
  """

  # Google-Maps format? Ex:
  # https://www.google.com/maps/place/Douai/@50.3680863,3.0812079,17.98z
  if "google.com" in location_raw:
    location_search = re.search('(@[^?/]+)$', location_raw)
    if not location_search:
      print("❌ Unable to find GPS coordinates in Google Maps URL")
      sys.exit(1)
    location_raw = location_search.group(1)

  # Google-Maps short comma-separated format? Ex:
  # @50.3680863,3.0812079,17.98z
  # 50.3680863,3.0812079,17.98z
  # 50.3680863,3.0812079
  location_search = re.search('^@?(\\d+[.]\\d+),(\\d+[.]\\d+)(,\\d+[.]\\d+z)?$', location_raw)
  if not location_search:
    print("❌ Unable to find GPS coordinates in location in substring")
    sys.exit(1)

  latitude = location_search.group(1)
  latitude_ref = 'N'
  longitude = location_search.group(2)
  longitude_ref = 'W'
  return (latitude, latitude_ref, longitude, longitude_ref)
