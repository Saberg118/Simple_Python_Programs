"""
This is a password generator that prompts the user the day the were born,
favoriteFruit, and first name. 
The new password will contain the the last two letters of their first name, 
the last digit of the day they were born times 3, first three letter of their favorit fruit, and
the first letter of their name capitalized.
The program will then display the new password to the user
"""

#Get the information needed from user needed to generate the password
day = [input("What was the day and month you were born ")]
favFruit = input("What is your favorite fruit ")
firstName = [input("What is your first name ")]

# get the last two letter of their first name and the first letter of their name capitalized
for letters in firstName:
    lasttwoLetters = letters[-2] + letters[-1]
    firstLetter = letters[0].upper()

# multiply the the last digit of the day they were born by three 
for num in day:
    lastNum = int(num[1])
    times3 = lastNum * 3

#get the firstthree letter of their favorite password
lastThree = (favFruit[0:3])

# Display new password
print(lasttwoLetters + str(times3) + lastThree + firstLetter)
