#This program will prompt the user to enter 100 numbers.
#The program will keep a running total 
#It will print the sum to the user at the end.

def main():

    total = 0
    
    for x in range(100):
         print('This is loop #' + str(x))
         number = input("Please enter a number: ")
         num = int(number)
         total += num
         
    print("The sum of these numbers are: " + str(total))


main()

counter = 0
i = 0
for i > number;