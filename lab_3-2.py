# author: LM (AMDG) 3/7/22
def factorial(number):
    total = 0
    while number > 0:
        if number > 0:
            total = number * (number - 1)
        else:
            break
    return total

number = int(input("What is the number: "))
print(factorial(number))
