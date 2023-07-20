# Import random module
import random

# Prints a random number that is between -1 and 10, does not include 10
# random.randrange(start, end)
# random.randint(start, including end)

# r = random.randrange(-5, 11)
# print(r)

# Variables typically have underscores between words
top_of_range = input("Type a number: ")

# check if input is a number
if top_of_range.isdigit():

    # convert String to Int ("25" -> 25)
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number larger than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0


# While loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        # continue will bring us back to top of loop
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
 
#  ELIF instead of else-if-else, happens after initial if statement is checked (removes nested if statement)
    elif user_guess > random_number:
        print("Oops, that's not right, sorry!")
        print("You were a little too high..")
    else:
        print("You were a little too low..")

         

print("You got it in", guesses, "guesses")