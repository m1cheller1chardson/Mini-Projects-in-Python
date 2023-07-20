name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You open your eyes and lift your head to the sky, blinded by the heavy light of the sun. You dust off the sand, and stand. You can go left, or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a large pond, a family of ducks swimming peacefully. Do you swim or walk around it?")
elif answer == "right":
    print()
else:
    print('Not a valid response. You lose.')