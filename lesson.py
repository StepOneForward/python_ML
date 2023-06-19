
nu = 1234
def funct (number: int):
    next = number % 10
    num = int(number / 10)
    if num > 0:
        result = (next * 10) + funct(num)
    return result

print(funct(nu))
