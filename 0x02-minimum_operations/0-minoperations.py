#!/usr/bin/python3
"""module to define minOperations function"""


def is_prime(n):
    """function to check if a number is prime"""
    if n < 2:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True


def primes_list(n):
    """function to generate a list of prime numbers"""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def minOperations(n):
    """function to calculate the minimum operations"""
    if n < 2:
        return 0
    primes = primes_list(n)
    nums = []
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                nums.append(prime)
                break
        n = n // prime

    return sum(nums)
