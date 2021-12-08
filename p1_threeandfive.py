def findMultiplesSums(multiples: list[int], limit: int) -> int:
    total: int = 0
    divisors: list[int] = []

    for i in range(limit): # increments to the limit
        for j in multiples: # iterates through the list of multiples to be checked
            if(i % j == 0): # checks if the number is a multiple of the value
                divisors.append(i)

    divisors = list(set(divisors)) # removes all duplicates
    total = sum(divisors)

    return total


if __name__ == "__main__":
    print(findMultiplesSums([3,5], 1000))
