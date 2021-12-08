from math import *
def checkPrime(val: int) -> bool:
    if (val == 1 or val == 0):
        return False

    for i in range(2, int(sqrt(val)+1), 1):
        if (val % i == 0):
            return False
    return True


def findNthPrime(nth: int) -> int:
    count: int = 0
    index: int = 0
    currentPrime: int = 0

    while(count != nth):
        if(checkPrime(index)):
            currentPrime = index
            count += 1
            print(f'{count}: {currentPrime}')
        index += 1

    return currentPrime

if __name__ == "__main__":
    print(findNthPrime(10001))
