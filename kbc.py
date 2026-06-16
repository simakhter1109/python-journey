# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

# First Try (How i did it)
question = [
    ["Which is the capital of India?",
     ["A. Bhubaneswar.", "B. Kolkata", "C. Mumbai", "D. Delhi"], 
     "D", 10000],

    ["What is the national animal of India?"
     ["A. Tiger", "B. Lion", "C. Dinosaur", "D. Dog"], 
     "A", 50000],
    
    ["Which planet is known as the red planet?",
     ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"], 
     "C", 10000],

    ["Who invented light?", 
     ["A. Thomad Edison", "B. Chalres Babbage", "C. Kayne West",  "D. Beyonce"], 
       "A", 60000],

    ["Who is the Primse Minister of India?",
     ["A. Rahul Gandhi",  "B. Mamta Banerjee", "C. Narendra Modi", "D. Justin Bieber"],
     "C", 100000],
]

amount_won = 0

print("Welcome to KBC")

for q in question:
    print("\n" + q[0])

    for option in q[1]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q[2]:
        amount_won = q[3]
        print(f" Correct! You won ₹{amount_won}")
    else:
        print("Wrong Answer!")
        break

print("\n Game Over!")
print(f"Final Amount You Take Home: ₹{amount_won}")
