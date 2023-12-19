"""
samlple tests

"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """test the calac madule."""

    def test_add_numbers(self):
        """test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """subtracting numnbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
