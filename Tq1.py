number = int(input())
number = number % 10
if(number % 3 == 0):
    print(number)
    print('Yes,It is Divisible')
else:
    print(number)
    print('No,It is not Divisible')
