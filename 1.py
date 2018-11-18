#!/usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def func(l, k):
    sums = []
    for index, element in enumerate(l):
        print(f'Current element: {element}')
        if index == 0:
            # first element - need another
            print()
            continue
        for num in range(index):
            print(f'Appending {l[index]} + {l[num]}')
            sums.append(l[num] + l[index])
        print()
    print(sums)
    return k in sums

print(func([10, 15, 3, 7], 17))
