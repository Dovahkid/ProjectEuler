from math import *

def findFactors(number: int) -> list[int]:
    factors: list[int] = []

    for i in range(1, ceil(sqrt(number))):
        if(number%i==0):
            factors.append(i)
            if (i != number/i):
                if(number/i != number):
                    factors.append(number/i)

    return factors


def findAmicableSums(limit: int) -> list[int]:
    factoredSum: int = 0
    amicableSum: int = 0
    amicableSumList: list[int] = []

    for i in range(1, limit):
        factoredSum = sum(findFactors(i))
        amicableSum = sum(findFactors(factoredSum))

        if(amicableSum == i):
            if (factoredSum != i):
                amicableSumList.append(i)

    return amicableSumList


def calc():
    amicableSums: list[int] = findAmicableSums(10000)
    sums: int = 0

    for i in amicableSums:
        sums += i

    return sums

if __name__ == "__main__":

    #for i in range(1, 100):
    #print(findFactors(220))

    print(calc())
