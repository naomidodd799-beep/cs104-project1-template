
print("Author: Naomi Dodd")
print()
print()
print("A quiz/questionnaire program built for CS 104 Project 1")


# TODO: Define your variables here.
score = 0
# TODO: Print a welcome message introducing your program.
print("Welcome to,Are you a gamer quiz!")
print()
print()
print("This quiz is to test the knowledge of gaming and technology use of the user.The user will answer five multiple choice questiones. Each answer would be stored in a variable and checked using conditional statments.Correct answers will be increase the users score. At the end of the quiz the user total score will determine the final message they received.")
print()
print()
# TODO: Write your questions and conditional logic here.
# Follow the outline you planned in your README.
print("1. What company makes the Playstation?")
print("1. Microsoft")
print("2. Sony")
print("3. Nintendo")

answer_one = input("Enter your answer: ")

if answer_one == "2":
    print("Correct")
    score = score + 1
elif answer_one == "1" or answer_one == "3":
    print("Incorrect!")
else:
    print("Invalid Choice.")

print()
print()

print("2. How many players from one basketball team can be on the court?")
print("1. 10")
print("2. 8")
print("3. 5")

answer_two = input("Enter your answer: ")

if answer_two == "3":
    print("Correct!")
    score = score + 1

elif answer_two == "1" or answer_two == "2":
    print("Incorrect!")
else:
    print("Invaild choice.")

print()
print()

print("3. Which device is mainly used to control a video game? ")
print("1. Controller")
print("2. Printer")
print("3. Pen")

answer_three = input("Enter your answer: ")

if answer_three == "1":
    print("Correct!")
    score = score + 1
elif answer_three == "2" or answer_three == "3":
    print("Incorrect!")
else:
    print("Invalid choice.")

print()
print()

print("4. Which game features the MyCAREER game mode?")
print("1. NBA 2K")
print("2. Mario Kart")
print("3. Fortnite")

answer_four = input("Enter your answer: ")

if answer_four == "1":
    print("Correct!")
    score = score + 1
elif answer_four == "2" or answer_four == "3":
    print("Incorrect!")
else:
    print("Invalid choice.")

print()
print()

print("\n5. Which of these is a gaming console?")
print("1. MacBook")
print("2. Lenovo")
print("3. PS5")

answer_five = input("Enter your answer: ")

if answer_five == "3":
    print("Correct!")
    score = score + 1
elif answer_five == "1" or answer_five == "2":
    print("Incorrect!")
else:
    print("Invalid choice.")

print("Your final score is", score, "out of 5.")

if score == 5:
    print("Perfect score! Great job!")
elif score >= 3 and score < 5:
    print("Good job!")
else:
    print("Keep practicing!")


# TODO: Display the final results to the user.
