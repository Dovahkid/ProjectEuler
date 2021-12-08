num = 0
for i in range(1,1001):
    num += i**i
num %= 10**10
print(num)