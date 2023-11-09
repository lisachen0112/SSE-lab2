import re
import numpy as np

def get_list_of_number(query):
    return [int(i) for i in re.findall(r'[0-9]+', query)]


def largest(nums):
    return str(max(nums))


def smallest(nums):
    return str(min(nums))


def addition(nums):
    return str(sum(nums))


def product(nums):
    return str(np.prod(nums))


def is_cube(n):
    cube_root = n**(1./3.)
    return round(cube_root) ** 3 == n


def is_square(n):
    cube_root = n**(1./2.)
    return round(cube_root) ** 2 == n


def square_cube(nums):
    for i in nums:
        if (is_cube(i)) and (is_square(i)):
            return str(i)


def is_prime(num):
    state = True
    if num <= 0:
        state = False
        return state
    else:
        for i in range(2, num):
            if num % i == 0:
                state = False
                break
        return state


def prime(nums):
    for num in nums:
        if is_prime(num):
            return str(num)


def subtraction(nums):
    return str(nums[0] - nums[1])
