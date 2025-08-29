                                    # Quiz App 
                                # Devyani Chaudhari

quiz_questions = [
    {
        "question": "Who is the current UN Secretary-General?",
        "options": ["António Guterres", "Ban Ki-moon", "Kofi Annan", "Joe Biden"],
        "answer": 1
    },
    {
        "question": "Which country hosted the 2024 Summer Olympics?",
        "options": ["France", "Japan", "USA", "Brazil"],
        "answer": 1
    },
    {
        "question": "Current President of the United States (2025)?",
        "options": ["Joe Biden", "Donald Trump", "Barack Obama", "Kamala Harris"],
        "answer": 2
    },
    {
        "question": "Which country recently landed on the Moon’s south pole?",
        "options": ["India", "China", "USA", "Russia"],
        "answer": 1
    },
    {
        "question": "Which nation won the 2023 Cricket World Cup?",
        "options": ["India", "Australia", "England", "Pakistan"],
        "answer": 2
    },
    {
        "question": "Which country is hosting the G20 Summit 2025?",
        "options": ["South Africa", "Brazil", "India", "Germany"],
        "answer": 2
    },
    {
        "question": "Who is the CEO of Tesla in 2025?",
        "options": ["Elon Musk", "Tim Cook", "Sundar Pichai", "Jeff Bezos"],
        "answer": 1
    },
    {
        "question": "Which country launched the Artemis program?",
        "options": ["USA", "China", "Russia", "India"],
        "answer": 1
    },
    {
        "question": "Which country hosted COP28 Climate Summit in 2023?",
        "options": ["UAE", "UK", "India", "USA"],
        "answer": 1
    },
    {
        "question": "Which country recently joined BRICS in 2024?",
        "options": ["Saudi Arabia", "Japan", "Mexico", "South Korea"],
        "answer": 1
    },
    {
        "question": "Which city will host Expo 2030?",
        "options": ["Riyadh", "Paris", "Rome", "Beijing"],
        "answer": 1
    },
    {
        "question": "Which company became the first to hit $4 trillion market cap?",
        "options": ["Apple", "Microsoft", "Google", "Amazon"],
        "answer": 2
    },
    {
        "question": "Which nation is building the Neom city project?",
        "options": ["Saudi Arabia", "UAE", "Qatar", "Oman"],
        "answer": 1
    },
    {
        "question": "Who is the current Prime Minister of India (2025)?",
        "options": ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh"],
        "answer": 1
    },
    {
        "question": "Which country won the 2024 UEFA Euro Cup?",
        "options": ["Spain", "England", "Germany", "Italy"],
        "answer": 1
    },
    {
        "question": "Which tech company introduced ChatGPT?",
        "options": ["OpenAI", "Google", "Meta", "Amazon"],
        "answer": 1
    },
    {
        "question": "Which nation is the largest oil producer in 2025?",
        "options": ["USA", "Saudi Arabia", "Russia", "Iran"],
        "answer": 1
    },
    {
        "question": "Which country has the fastest-growing economy in 2025?",
        "options": ["India", "China", "USA", "Vietnam"],
        "answer": 1
    },
    {
        "question": "Where will the 2026 FIFA World Cup be held?",
        "options": ["USA, Canada, Mexico", "Qatar", "France", "China"],
        "answer": 1
    },
    {
        "question": "Who is the current UK Prime Minister (2025)?",
        "options": ["Rishi Sunak", "Keir Starmer", "Boris Johnson", "Liz Truss"],
        "answer": 2
    }
]

score = 0

print("Welcome to the My Quiz!\n")
for i, q in enumerate(quiz_questions, 1):
    print(f"Q{i}: {q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"  {idx}. {option}")
    try:
        choice = int(input("Enter your answer (1-4): "))
        if choice == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['options'][q['answer']-1]}\n")
    except:
        print("Invalid input. Skipping question.\n")

print(f" Quiz Completed! Your Score: {score}/{len(quiz_questions)}")
 "Vietnam"],
        "answer": 1
    },
    {
        "question": "Where will the 2026 FIFA World Cup be held?",
        "options": ["USA, Canada, Mexico", "Qatar", "France", "China"],
        "answer": 1
    },
    {
        "question": "Who is the current UK Prime Minister (2025)?",
        "options": ["Rishi Sunak", "Keir Starmer", "Boris Johnson", "Liz Truss"],
        "answer": 2
    }
]

score = 0

print("Welcome to the My Quiz!\n")
for i, q in enumerate(quiz_questions, 1):
    print(f"Q{i}: {q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"  {idx}. {option}")
    try:
        choice = int(input("Enter your answer (1-4): "))
        if choice == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['options'][q['answer']-1]}\n")
    except:
        p