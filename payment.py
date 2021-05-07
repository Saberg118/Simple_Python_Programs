"""
This program prompts for a 16 digit credit card number 
Verifies the use's input is 16 digits of integers
Displays the credit card company based on the first digti to the user
If no credit card company can be identified it notifies the user that its an unkown card
"""
try: 
   credit_card = int(input("Please input a 16-digit credit card number: "))
except ValueError:
    print("Error: you entered letters")
else:
    credit_card = str(credit_card)
    if len(str(credit_card)) == 16:
        if credit_card.startswith("4"):
            print("Visa")
        elif credit_card.startswith("5"):
             print("Mastercard")
        elif credit_card.startswith("6"):
            print("Discover")
        else:
            print("Unknown Card")
    else:
        print("This is not a 16-digit card")
