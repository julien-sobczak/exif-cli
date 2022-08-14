import unittest
from utils import format_date, parse_location


class TestUtils(unittest.TestCase):

    def test_format_date_default(self):
        self.assertEqual(format_date("1985"), '1985:01:01 12:00:00+00:00')
        self.assertEqual(format_date("1985:09"), '1985:09:01 12:00:00+00:00')
        self.assertEqual(format_date("1985:09:29"), '1985:09:29 12:00:00+00:00')
        self.assertEqual(format_date("1985:09:29 04:00"), '1985:09:29 04:00:00+00:00')
        # Dash is supported too for the year
        self.assertEqual(format_date("1985-09"), '1985:09:01 12:00:00+00:00')
        self.assertEqual(format_date("1985-09-29"), '1985:09:29 12:00:00+00:00')
        self.assertEqual(format_date("1985-09-29 04:00"), '1985:09:29 04:00:00+00:00')

    def test_format_date_unique(self):
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:01+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:02+00:00')
        self.assertEqual(format_date("1985", unique=False), '1985:01:01 12:00:00+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:03+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:04+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:05+00:00')
        for i in range(6, 60):
            self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:00:%s+00:00' % "{:02d}".format(i))
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:01:00+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:01:01+00:00')
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:01:02+00:00')
        for i in range(3, 60):
            self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:01:%s+00:00' % "{:02d}".format(i))
        self.assertEqual(format_date("1985", unique=True),  '1985:01:01 12:02:00+00:00')

    def test_parse_location(self):
        # Google-Maps URLs
        (lat, latr, lng, lngr) = parse_location("https://www.google.com/maps/place/Douai/@50.3680863,3.0812079,17.98z")
        self.assertEqual(lat, "50.3680863")
        self.assertEqual(latr, "N")
        self.assertEqual(lng, "3.0812079")
        self.assertEqual(lngr, "W")

        # Short-syntax
        (lat, latr, lng, lngr) = parse_location("@50.3680863,3.0812079,17.98z")
        self.assertEqual(lat, "50.3680863")
        self.assertEqual(latr, "N")
        self.assertEqual(lng, "3.0812079")
        self.assertEqual(lngr, "W")
        (lat, latr, lng, lngr) = parse_location("50.3680863,3.0812079,17.98z")
        self.assertEqual(lat, "50.3680863")
        self.assertEqual(latr, "N")
        self.assertEqual(lng, "3.0812079")
        self.assertEqual(lngr, "W")
        (lat, latr, lng, lngr) = parse_location("50.3680863,3.0812079")
        self.assertEqual(lat, "50.3680863")
        self.assertEqual(latr, "N")
        self.assertEqual(lng, "3.0812079")
        self.assertEqual(lngr, "W")

if __name__ == '__main__':
    unittest.main()
