# coding=utf-8
import argparse
import os
import sys
from exif import Image
from .utils import format_date, parse_location


def add_exif(files = [], date=None, location=None, date_unique=False, override=False):

    # Check files are specified as input
    if not files:
        print("❌ No file specified in argument.")
        print("👋 Exiting...")
        sys.exit(1)

    # Check files exist
    for filename in files:
        if not os.path.isfile(filename):
            print("❌ File %s doesn't exist." % filename)
            print("👋 Exiting...")
            sys.exit(1)

    # Process file
    for filename in files:
        print("📸 Processing %s..." % os.path.basename(filename))

        # Read file
        with open(filename, 'rb') as image_file:
            my_image = Image(filename)
            exif_attributes = my_image.list_all()

            # Set date
            if date:
                if 'datetime_original' in exif_attributes:
                    print("🙈 Date/Time Original already set: %s" % my_image.datetime_original)
                else:
                    my_image.datetime_original = format_date(date, date_unique)
                    print("✅ Set time to %s" % my_image.datetime_original)

            # Set location
            if location:
                if 'gps_latitude' in exif_attributes or \
                   'gps_latitude_ref' in exif_attributes or \
                   'gps_longitude' in exif_attributes or \
                   'gps_longitude_ref' in exif_attributes:
                    print("🙈 GPS location already set: %s %s, %s %s" % (my_image.gps_latitude, my_image.gps_latitude_ref, my_image.gps_longitude, my_image.gps_longitude_ref))
                else:
                    (my_image.gps_latitude, my_image.gps_latitude_ref, my_image.gps_longitude, my_image.gps_longitude_ref) = parse_location(location)
                    print("✅ Set location to %s %s, %s %s" % (my_image.gps_latitude, my_image.gps_latitude_ref, my_image.gps_longitude, my_image.gps_longitude_ref))

        # Override file
        out_filename = None
        if override:
            out_filename = filename
        else:
            out_filename = os.path.join(os.path.dirname(filename), "modified_" + os.path.basename(filename))
        with open(out_filename, 'wb') as new_image_file:
            new_image_file.write(my_image.get_file())
            print("💾 Saved %s" % os.path.basename(out_filename))

