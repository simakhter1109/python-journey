score = 0

answer = input("What is the capital of India?")
if answer.lower() == "new delhli":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is New Delhi.")
answer = input("Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("Which is the largest ocean?")

if answer.lower() == "Pacific Ocean".lower():
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("Which animal is called the King of the Jungle? ")

if answer.lower() == "lion":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is the national bird of India? ")

if answer.lower() == "peacock":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is the largest planet in our solar system? ")

if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("\nQuiz Over!")
print("Your Score:", score)
if score >= 8:
    print("Excellent!")
elif score >= 5:
    print("Good Job!")
else:
    print("Keep Practicing!")