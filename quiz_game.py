print("Welcome to my computer quiz!")

# Variable - playing
# Inside () is the PROMPT - whatever user types belongs to the prompt
# This is how to retrieve user input
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    # QUIT() immediately terminates the program
    print("Okay, goodbye.")
    quit()

print("Okay! Let's play :D ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
