# Defining fuctions
print (" ")
def numeric_to_letter_grade(grade):
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')
grade = int(input('Please enter numeric grade: '))
#calling numeric_to_letter_grade define above
print(" ")
numeric_to_letter_grade(grade)
            
