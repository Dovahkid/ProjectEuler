from math import *

def findFactors(number: int) -> list[int]:
    factors: list[int] = []

    for i in range(1, ceil(sqrt(number))):
        if(number%i==0):
            factors.append(i)
            if (i != number/i):
                factors.append(number/i)

    return factors


def checkPrime(val: int) -> bool:
    if (val == 1 or val == 0):
        return False

    for i in range(2, int(sqrt(val)+1), 1):
        if (val % i == 0):
            return False
    return True


if __name__ == "__main__":
    factors: list[int] = []
    primeFactors: list[int] = []

    factors = findFactors(600851475143)

    for i in factors:
        if(checkPrime(i)):
            primeFactors.append(i)

    print(primeFactors[len(primeFactors)-1])



