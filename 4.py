#!/usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def func(in_array):
    positive_numbers = [number for number in in_array if number >= 0]
    # No positive numbers found return 0
    if not positive_numbers:
        return 0
    positive_numbers.sort()
    biggest_num = max(positive_numbers)
    # Starting from 1, make sure each number up until the biggest number in the list is present if not return it
    for i in range(biggest_num):
        if i + 1 not in positive_numbers:
            return i + 1
    # We found all numbers up until the max return max + 1
    return biggest_num + 1

print(func([3, 4, -1, 1]))
print(func([1, 2, 0]))
print(func([-1, -2, -1]))
print(func([-1, -2, 0]))