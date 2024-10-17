#!/usr/bin/python3
"""module to define minOperations function"""


def minOperations(n):
    """Function to calculate the minimum operations based on prime factors"""
    if n < 2:
        return 0

    num_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            num_operations += factor
            n = n // factor
        factor += 1

        if factor > 2 and factor % 2 == 0:
            factor += 1

    return num_operations
