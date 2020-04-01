# This driver file finds the largest prime within
# a minute and prints it.
#
# Change line 36 to desired algorithm, i.e. brute(n).
# WARNING! Lucas-lehmer cannot be used.
#
# Make sure fermat and millerRabin are written as
# <function>(n, 10). Where 10 is k, the second parameter

import time

# from FILE import FUNCTION
from brute import brute
from smart_brute import smartBrute
from lucas import lehmer
from fermat import fermat
from mil_rab import millerRabin


def driver():
    n = 2
    primes = []
    timelimit = time.time() + 60  # 60 seconds
    while time.time() < timelimit:
        if primeTest(n):
            # Make sure the prime was still within the timelimit
            if time.time() < timelimit:
                primes.append(n)
            else:
                break
        n += 1
    print(max(primes))


def primeTest(n):
    if smartBrute(n):  # Algorithm change here
        return True
    return False


if __name__ == "__main__":
    driver()
