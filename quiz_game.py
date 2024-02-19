print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphics Processing Unit'.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Random Access Memory'.")

answer = input("What does ROM stand for? ")
if answer.lower() == "read-only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Read-Only Memory'.")

answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphical User Interface'.")

print("Your final score is:", score)
print("Your percentage is:", ((score/5)*100)+"%")
