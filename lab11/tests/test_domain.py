import unittest

from domain.passanger import Passanger
from domain.plane import Plane

class TestPlane(unittest.TestCase):
    def plane_test(self):
        self.plane = Plane(
            number = 1,
            company = 'Zburam SRL',
            seats = 37,
            destination = 'Resedinta Majeri',
            passangers = ['Majeri Robert 123']
        )
    
    def test_attributes(self):
        self.assertEqual(self.plane.get_number(), 1)
        self.assertEqual(self.plane.get_company(), 'Zburam SRL')
        self.assertEqual(self.plane.get_seats(), 37)
        self.assertEqual(self.plane.get_destination(), 'Resedinta Majeri')
        self.assertEqual(self.plane.get_passangers(), 'Majeri Robert 123')