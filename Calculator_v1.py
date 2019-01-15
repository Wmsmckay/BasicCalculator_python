# add two numbers
def add(a, b):
    return a + b

# subtract the numbmers
def subtract(a, b):
    return a - b

# miltiply the numbers
def multiply(a, b):
    return a * b

#divide the numbers
def divide(a, b):
    return a / b

#print the menu
def printMenu():
    print("Choose an operation")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("")

cont = 'y'


# run the program
while cont == 'y':
    printMenu()
    # choose option from the menu
    option = int(input())
    #get input from the user
    num1 = int(input("Please enter a number: "))
    num2 = int(input("please enter another number: "))

    if option == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif option == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif option == 3:
        print(num1, "x", num2, "=", multiply(num1, num2))
    elif option == 4:
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

    input("Press enter to continue...")
    
    cont = input("Would you like to calculate again?[y/n]: ")
    print()

print("Thank you for playing")
