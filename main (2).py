quiz_data = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who wrote the national anthem of India?",
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra", "C. Mahatma Gandhi", "D. Subhash Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Program Unit"],
        "answer": "B"
    },
]

def run_quiz(quiz_data):
    score = 0
    for question in quiz_data:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == question["answer"]:
            print(" Correct! you got this!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {question['answer']}")
    print(f"\n You got {score} out of {len(quiz_data)} correct.")

run_quiz(quiz_data)
