def odd_number(number):
    return [odd for odd in range(number) if int(odd % 2) != 0]


print(odd_number(20))