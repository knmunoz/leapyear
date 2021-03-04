import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.leapyear(2000), "{0} is a leap year".format(2000))


if __name__ == "__main__":
    unittest.main(verbosity=2)    