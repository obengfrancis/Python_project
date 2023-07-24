#While loop with user input

#print("-----------------------------------")
#print("While loop with user input")
#print("-----------------------------------")

#inp = input('Hi! please say hello')
#while inp != 'hello':
 #       inp = input('Please say hello')
  #      print('It\'s about time')

print("-----------------------------------")
print("While loop exercise")
print("-----------------------------------")

password = " "

while password != "secret":

        password = input("Please enter password: ")

        if password == "secret":
            print("Welcome")
        else:
            print("Sorry, the password you entered is incorrect. Please try againg")
