import NUKES
import unittest

class TestNukes(unittest.TestCase):
    def test_representValueIn_for_number_systems_below_two_returns_null(self):
        self.assertEqual([], NUKES.Nukes().representValueIn(5,1));
        self.assertEqual([], NUKES.Nukes().representValueIn(5,0));
        
    def test_representValueIn_returns_the_input_decimal_value_in_the_given_representation(self):
        self.assertEqual([1, 0, 1], NUKES.Nukes().representValueIn(5,2));

    def test_representValueIn_for_decimal_system_returns_the_same_value_each_char_separated_in_reverse_order(self):
        self.assertEqual([5], NUKES.Nukes().representValueIn(5,10));
        self.assertEqual([0, 1], NUKES.Nukes().representValueIn(10,10));
        self.assertEqual([0, 1, 5, 6, 4, 2, 4, 6], NUKES.Nukes().representValueIn(64246510,10));


    def test_get_chamber_status(self):
        self.assertEqual('1 0 1 0 0 ', NUKES.Nukes().getChanbersStatus(5,1,5));
        

if __name__ == '__main__':
    unittest.main()

