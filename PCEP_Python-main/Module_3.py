var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# n = int(input("Enter a number: "))
# print(n >= 100)



x = int(input("Input Num 1: "))

y = int(input("Input Num 2: "))

if x > y:
    largeNum = x
    
else:
    largeNum = y
    
print("The largest number, is:" + str(largeNum))

x = input("Please, input the name of a flower: ")

if (x == "Spathiphyllum"):
    print(f'{x} is the best plant ever!')
elif (x == "pelargonium"):
    print(f'Spathiphyllum! Not pelargonium!')
else:
    print(f'No, I want a big Spathiphyllum!')


income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")


while True:
    print("I'm stuck inside a loop.")


# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Please, guess a number randomly\n"))

while number:
    if number == secret_number:
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Please, guess a number randomly\n"))
         
print("Well done, muggle! You are free now.")


i = 0
while i < 100:
    # do_something()
    i += 1


for i in range(10):
    print("The value of i is currently", i)


for i in range(2, 8):
    print("The value of i is currently", i)


for i in range(2, 8, 3):
    print("The value of i is currently", i)


for i in range(1, 1):
    print("The value of i is currently", i)


power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


import time

# Write a for loop that counts to five.
for i in range(5):
    print(i+1, " Mississippi")
    time.sleep(1)
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")



# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")



word = str(input("Please enter a word. Enter chupacabra to exit ..."))

while word != "chupacabra":
    if word == "chupacabra":
        break
    word = str(input("Please enter a word. Enter chupacabra to exit ..."))



# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = str(input("Please enter a word. I eat vowels ... \n"))

for letter in user_word:
    # Complete the body of the for loop.
    user_word = user_word.upper()
    for x in user_word:
        if x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
            user_word = user_word.replace(x, '')
        else:
            continue

print(user_word)

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

for i in range(5):
    print(i)
else:
    print("else:", i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)


blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_needed = 1
#
while blocks >= blocks_needed:
    blocks = blocks - blocks_needed
    blocks_needed = blocks_needed + 1
    height = height + 1
#	

print("The height of the pyramid:", height)



c_0 = int(input("Please input a positive number : "))
steps = 0

while c_0 > 1:
    if c_0 % 2 == 0:
        c_0 = c_0 / 2
        steps = steps + 1
        
    else:
        c_0 = 3*c_0+1
        steps = steps + 1
    
    print(c_0)
    
else:
    print("The number of steps is", steps)
    print("The collatz dance is over!")



# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1


text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print(i)

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

for digit in "0165031806510":
    if digit == "0":
        print('x', end="")
        continue
    print(digit, end="")

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num)

for i in range(0, 6, 3):
    print(i)


# Wow, bro 
