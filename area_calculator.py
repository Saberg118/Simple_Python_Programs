"""
This program will compute the area of either a square or triangle. 
The program will:
1. Prompt the user to select a shape
2. Validate the user's input 
3. Calculate area of that shape
4. Print the area of that shape to the area

"""

import math

def message():
    print("Welcome to the Area Calculator: ")
    name = input("What is your name? ")  
    print("Hello " + str(name))

def get_shape(): 
    option = input("Enter C for Circle or T for Triangle: ")
    selection = option.upper() 
    return selection

def calculate_area(selection):
    if selection == 'C':
        radius = int(input("What is the radius of the circle? "))
        circle_area = math.pi * radius ** 2
        print(format(circle_area, '.2f'))

    elif selection == 'T':
        base = int(input("What is the base of triangle? "))
        height = int(input("What is the height of the triangle? "))
        triangle_area = (base * height) / 2
        print(format(triangle_area, '.2F'))
    
    else:
        print("You did not provide a correct input")
        print("Please try again")
        retry()

def retry():
    shape = get_shape()
    calculate_area(shape)

def main():
    message()
    shape = get_shape()
    calculate_area(shape)

main()
