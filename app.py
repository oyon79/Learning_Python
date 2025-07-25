#Printing a message by print function to console

print("Hello, world!")
print('O----')
print(' ||||')
print('*' *10)


price = 10
rating = 4.9
name = 'Sahriar'
is_published = True
print(price)
print(rating)
print(name)
print(is_published)

full_name = 'Sahriar Hossain'
age = 22
is_new = True
print(full_name)
print(age)
print(is_new)


#Recieving a input message by input function to console
name = input('What is your name? ' )
fav_color = input('What is your favourite color? ')
print(name+ ' likes ' + fav_color)

#Type conversion
birth_year = input('Birth year: ')
age = 2025 - int(birth_year)
print(age)

#converting weight from lbs to kg
weight_lbs = input('weight(lbs): ')
weight_kg = 0.45 * int(weight_lbs)
print(weight_kg)

#working with strings
course_1 = "Python's For Beginners"
print(course_1)
course_2 = 'python For "Beginners" '
print(course_2)

#printing Multiline strings
course_3 = '''
Hlw,
Myself Md.Sahriar Hossain .
It's a python course.
I am a "python" developer.
'''
print(course_3)
print(course_1[0])  # Accessing first character
print(course_1[-1]) # Accessing last character
print(course_1[-2]) # Accessing 2nd character from last
print(course_1[0:5]) # means [starting index : ending index]
print(course_1[1:5])
print(course_1[3:]) 
print(course_1[:5])
print(course_1[1:-1]) # means [starting index : ending index] excluding start and end index


first = 'Sahriar'
last = 'Oyon'
msg = f'{first} [{last}] is a coder'
print(msg) 

course = 'Python for Beginners'
print(len(course))  # Length of the string
print(course.upper())  # Convert to uppercase
print(course.lower())  # Convert to lowercase

print(course.find('P') )  # Find the index of 'P'
print(course.find('O'))  # Find a character that does not exist, returns -1
print(course.find('Beginners'))  # Find the index of 'Beginners'
print(course.replace('Beginners', 'Absolute Beginners'))  # Replace a substring

print('Python' in course)  # Check if 'Python' is in the string, returns True (boolean)


#Arithmetic operations (// = floor division) (** = to the power) 
x = 10
x += 3
print(x)
y = 10
y -= 3
print(y)

x = 10 + 3 * 2 ** 2
print(x)  # Output: 10 + 3 * 4 = 10 + 12 = 22
x = (10 + 3) * 2 ** 2
print(x)  # Output: (10 + 3) * 4 = 13 * 4 = 52
x = (2 + 3) * 10 - 3 # Output: (2 + 3) * 10 - 3 = 5 * 10 - 3 = 50 - 3 = 47
print(x)  # Output: 47

#Math functions
x = 2.9
print(round(x))  # Round to the nearest integer
print(abs(-2.9))  # Absolute value

import math
print(math.ceil(2.9)) # Ceiling value
print(math.floor(2.9))  # Floor value

#if statements
is_hot = True
if is_hot:
  print("It's a hot day")
print("Enjoy your day")

