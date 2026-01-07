questions = ("What is the capital of France?",           
            "What is 2 + 2?", 
            "What is the largest planet in our solar system?", 
            "Who wrote 'Romeo and Juliet'?", 
            "What is the boiling point of water in Celsius?")

options = (("A. London", "B. Paris", "C. Berlin", "D. Madrid"),
        ("A. 3", "B. 4", "C. 5", "D. 6"),
        ("A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"),
        ("A. Shakespeare", "B. Dickens", "C. Austen", "D. Hemingway"),
        ("A. 100°C", "B. 90°C", "C. 80°C", "D. 70°C"))

answers = ("B", "B", "A", "A", "A")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    user_guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(user_guess)

    if user_guess == answers[question_num]:
            score += 1
            print("Correct!")
    else:
            print("Wrong!")
            print(f"The correct answer is: {answers[question_num]}")

    question_num += 1

print("----------------------------")
print("           RESULTS          ")
print("----------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

final_score = int((score / len(questions)) * 100)
print(f"Your final score is: {final_score}%")
