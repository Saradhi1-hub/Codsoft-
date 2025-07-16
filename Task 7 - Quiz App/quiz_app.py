# Quiz App - Console based

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Hyderabad", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used to build Android apps?",
        "options": ["A. Kotlin", "B. Python", "C. Swift", "D. C#"],
        "answer": "A"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Accept Memory", "D. Ready Available Memory"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of Python?",
        "options": ["A. Guido van Rossum", "B. Dennis Ritchie", "C. James Gosling", "D. Linus Torvalds"],
        "answer": "A"
    }
]

score = 0

print("🧠 Welcome to the Quiz App!\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}\n")

print(f"🎉 You scored {score} out of {len(questions)}.")
