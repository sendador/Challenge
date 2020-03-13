import unittest
from chapter_1 import Car, IllegalCarError


class TestSum(unittest.TestCase):
    def setUp(self):
        self.c = Car(4, 2000, 5)

    def tearDown(self):
        del self.c

    def test_insert_correct_car(self):
        self.assertEqual(self.c.pax_count, 4)
        self.assertEqual(self.c.car_mass, 2000)
        self.assertEqual(self.c.gear_count, 5)

    def test_total_mass_function(self):
        self.assertEqual(self.c.total_mass(), 2280)


if __name__ == '__main__':
    unittest.main()
