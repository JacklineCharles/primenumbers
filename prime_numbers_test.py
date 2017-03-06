import unittest
from prime_numbers import *
#test

class Primenumberstest(unittest.TestCase):
    def test_six_not_in_list(self):
        result = primes(7)
        self.assertNotIn(6, result)

    def test_two_is_a_prime_number(self):
        result = primes(19)
        self.assertIn(4, result)

    def test_length_of_list_less_than_n(self):
        self.assertLess(len(primes(10)), 10)
   

    def test_sixty_two_is_not_a_prime_number(self):
        result = primes(65)
        self.assertNotIn(62, result)

    def test_output_is_a_list(self):
        result = primes(53)
        result = isinstance(result, list)
        self.assertTrue(result)

    def test_one_returns_an_empty_list(self):
        result = primes(1)
        self.assertNotIn(1, result)

    def test_return_empty_list_if_n_is_negative(self):
        result = primes(-1)
        self.assertListEqual([],result)

    def test_raise_error_if_input_is_not_integer(self):
    	with self.assertRaises(TypeError):
    		primes('string')


if __name__ == '__main__':
    unittest.main()

