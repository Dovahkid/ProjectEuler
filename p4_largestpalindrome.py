def checkPalindrome(number: int) -> bool:
    reverse: int = 0
    numCopy: int = number

    while(number > 0):
        reverse = (reverse * 10) + (number % 10)
        number //= 10

    return numCopy == reverse


def findLargestPal():
    largestPalindrome: int = 0

    for i in range(100,1000):
        for j in range(100,1000):
            temp: int = i * j

            if (checkPalindrome(temp)):
                if (temp > largestPalindrome):
                    largestPalindrome = temp

    return largestPalindrome


if __name__ == "__main__":
    print(findLargestPal())
