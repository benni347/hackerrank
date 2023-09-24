#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This should validated postal codes.

Problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true

:author: Cedric Skwar <cdrc@5y5.one>
:license: GNU General Public License v3 or later (GPLv3+)
"""


def precompute_primes_and_sums(max_n: int):
    """Precompute prime numbers and their prefix sums up to max_n."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    prime_sum = [0] * (max_n + 1)

    p = 2
    sum_so_far = 0
    while p <= max_n:
        if is_prime[p]:
            sum_so_far += p
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False

        prime_sum[p] = sum_so_far
        p += 1

    return prime_sum


# Precompute primes and their sums up to the maximum upper_bound.
MAX_UPPER_BOUND = 10**6
prime_sum = precompute_primes_and_sums(MAX_UPPER_BOUND)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        upper_bound = int(input().strip())
        print(prime_sum[upper_bound])
