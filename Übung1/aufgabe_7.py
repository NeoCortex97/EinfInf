# -*- coding: utf-8 -*-
# Write a program that reads an integer from user and prints the first prime numbers
# Part A: Write a program that can check if a number is prime
# PArt B: Write a program that reads an int and loops through the numbers until the entered amount of prime numbers is
#         found
import sys


def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def find_prime(start):
    tested = start
    while not check_prime(tested):
        tested += 1
    return tested


def find_first_n_primes(number):
    nums = []
    for i in range(number):
        if len(nums) > 0:
            nums.append(find_prime(nums[-1] + 1))
        else:
            nums.append(find_prime(2))
        sys.stdout.write(".")
    return nums


def main():
    number = input("[NUMBER]> ")
    if int(number) >= 1:
        sys.stdout.write("Working")
        prime_list = find_first_n_primes(int(number))
        sys.stdout.write("\n|")
        orig_count = 10
        count = orig_count
        for p in prime_list:
            sys.stdout.write("{:^10}|".format(p))
            count -= 1
            if count == 0:
                sys.stdout.write("\n|")
                count = orig_count
    else:
        print("1 is not a valid prime, so there are none!")


if __name__ == "__main__":
    main()
