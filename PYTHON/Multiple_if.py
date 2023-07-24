#Program to evaluate user input

print('==============================================')
print (" ")
number = input('Please enter an integer: ')

try:
    number = int(number)
    if(number > 20):
        print('Your input is ' + str(number) + ' > 20 ')
    if(number > 10 ):
        print('Your input is ' + str(number) + ' > 10 ')
    if (number > 0):
        print('Your input is ' + str(number) + ' > 0 ')
    if(number < 0 ):
        print('Your input is ' + str(number) + ' is negative')
    print(" ")
except ValueError as e:
    print('Your input is not an integer')
    
