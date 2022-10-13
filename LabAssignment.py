def print_hello(icecream):
    print(icecream)

icecream = input("What flavor of icecream would you like? strawberry, vanilla, chocolate, mint")
options = ["strawberry", "vanilla", "chocolate", "mint"]
if (icecream == options[0]):
    print("Here is your strawberry icecream!")
    print_hello("Have a nice day!")
elif (icecream == options[1]):
    print ("Here is your vanilla icecream!")
    print_hello("Goodbye!")
elif (icecream == options[2]):
    print ("Here is your chocolate icecream!")
    print_hello("Peace!")
elif (icecream == options[3]):
    print ("Here is your mint icecream!")
    print_hello("See you again soon!")

# print_hello("butter");