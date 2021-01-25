import math
def count_zeroes(n):
    print(len(str(math.factorial(n)))-len(str(math.factorial(n)).strip("0")))
n = int(input())
count_zeroes(n)
