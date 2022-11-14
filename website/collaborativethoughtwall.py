# the idea is that this would be a wall where people can write either one character or one word. I think Zaid's python class can help with this. If keypress is space then they are done.
# If word is greater than 10 characters user is done,

def add_characters():
    totalComplete = False
    while True:
        inp = input("Enter one chacter").upper()
        if len(inp) > 1:
            print("You used more than one character try again.")
        if len(inp) == 1:
            print("Awesome you have done it.")
            totalComplete = True
        else:
            print("Please enter a character.")

