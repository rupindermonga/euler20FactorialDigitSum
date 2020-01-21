#calculating sum of all digits of n!

def CalculatingFactorial(n):
    result = 1
    for number in range(n,1,-1):
        result *= number
    return result


def FactorialDigitSum(n):
    result = CalculatingFactorial(n)
    sum = 0
    while result >0:
        Remainder = result % 10
        sum += Remainder
        result //= 10
    return sum

final = FactorialDigitSum(100)
print(final)