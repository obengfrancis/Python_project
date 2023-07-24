#Using loops in Python


print ("    ")

print ("Creating loops")
print ("=============================")

#defining list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#to store even numbers
even_numbers = []

even_count = 0

#iterate over list
for number in numbers:

#test if number is even
    if(number % 2 == 0):

#append to even numbers list
        even_numbers.append(number)


#increment count
    #even_count += 1

    print(even_numbers)

    #print("There are", even_count, "numbers in the list")
    
