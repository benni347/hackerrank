import unittest
from sumofprimes import precompute_primes_and_sums


class TestSumOfPrimes(unittest.TestCase):
    def test_sum_below_prime(self):
        self.assertEqual(precompute_primes_and_sums(10**6)[5], 10)
        self.assertEqual(precompute_primes_and_sums(10**6)[10], 17)
        self.assertEqual(precompute_primes_and_sums(10**6)[20], 77)
        self.assertEqual(precompute_primes_and_sums(10**6)[1], 0)
        self.assertEqual(precompute_primes_and_sums(10**6)[2], 2)
        self.assertEqual(precompute_primes_and_sums(10**6)[0], 0)


if __name__ == "__main__":
    unittest.main()
