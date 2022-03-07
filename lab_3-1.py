# auhtor: LM (AMDG) 3/7/22
#funstion that finds total from a list 
def r_max(nested_numberlist):
    total = 0
    for number in nested_numberlist:
        total += number
        #if there is a nested list
        if type(number) == list:
            #recursion
            total += r_max(number)
        else:
            total += number
    return total
