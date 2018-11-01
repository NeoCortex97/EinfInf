# -*- coding: utf-8 -*-
# Write a program that reads an integer from user and prints the first prime numbers
# Part A: Write a program that can check if a number is prime
# PArt B: Write a program that reads an int and loops through the numbers until the entered amount of prime numbers is
#         found
import sys


def check_prime(number):
    """Checks if a positive integer number is prime by looping through all smaller numbers and testing if
       the tested number is dividable by the lower ones. returns a bool if the number is prime"""
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def find_prime(start):
    """ Checks all positive integers from start until one is a prime. returns a prime number"""
    tested = start
    while not check_prime(tested):
        tested += 1
    return tested


def find_first_n_primes(number):
    """ finds the first n primes specified by number. returns a list of primes"""
    nums = []
    for i in range(number):
        if len(nums) > 0:
            nums.append(find_prime(nums[-1] + 1))
        else:
            nums.append(find_prime(2))
        sys.stdout.write(".")
    return nums


def print_results(numbers, line_length):
    """ Prints a rudimentary table of the results. returns nothing"""
    count = line_length
    for p in numbers:
        sys.stdout.write("{:^10}|".format(p))
        count -= 1
        if count == 0:
            sys.stdout.write("\n|")
            count = line_length


def main():
    number = input("[NUMBER]> ")
    if int(number) >= 1:
        sys.stdout.write("Working")
        prime_list = find_first_n_primes(int(number))
        sys.stdout.write("\n|")
        print_results(prime_list, 10)
    else:
        print("1 is not a valid prime, so there are none!")


if __name__ == "__main__":
    main()
