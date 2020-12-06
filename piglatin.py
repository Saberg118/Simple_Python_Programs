"""
Pig Latin is a language game, where you move the first letter of the word to the end and add “ay” 
So “Python” becomes “ythonpay.” To write a Pig Latin translator in Python. If the word begins
with a vowel then you just add "ay" to the end of the word
here are the steps we’ll need to take:
1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Check to see if the first letter is a vowel or consonants
3. Convert the word from English to Pig Latin.
4. Display the translation result.

This program is using python3.
Kiera Walsh
"""
vowels = ('a','e','i','o','u','A','E','I','O','U') #variable for vowels
pyg = 'ay' #variable to end with aye

original = input('Enter a word:') #get input from user

if original.startswith(vowels): #check to see if the first letter is a vowel
    word = original.lower() 
    first = word[0] #get the first letter in the word
    new_word = str(word) + str(first) + str(pyg) #concatenating first word and aye
    print(new_word)

elif len(original) > 0 and original.isalpha(): #word validation
  word = original.lower() 
  first = word[0] #get the first letter in the word
  new_word = str(word) + str(first) + str(pyg) #concatenating first word and aye 
  new_word = new_word[1:len(new_word)] #removing first letter of word
  print(new_word) #displaying translation

else:
  print('empty') #runs if input is empty or contains a number or special character
