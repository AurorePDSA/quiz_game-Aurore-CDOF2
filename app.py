import random

def ask_question(question, correct_answers):
    print(question)
    user_answer = input("Your answer: ").lower()
    return user_answer in map(str.lower, correct_answers)

def play_quiz():
    questions = [
        {"question": "What is the capital of France?", "answers": ["Paris"]},
        {"question": "Which planet is known as the Red Planet?", "answers": ["Mars"]},
        {"question": "What is the largest mammal in the world?", "answers": ["Blue Whale", "Whale"]},
        {"question": "How many continents are there?", "answers": ["7", "seven"]},
        {"question": "Who wrote 'Romeo and Juliet'?", "answers": ["William Shakespeare", "Shakespeare"]},
        {"question": "What is the chemical symbol for gold?", "answers": ["Au"]},
        {"question": "Which country is home to the kangaroo?", "answers": ["Australia"]},
        {"question": "What is the tallest mountain in the world?", "answers": ["Mount Everest"]},
        {"question": "Who painted the Mona Lisa?", "answers": ["Leonardo da Vinci", "Da Vinci"]},
        {"question": "What is the largest ocean in the world?", "answers": ["Pacific Ocean", "Pacific"]},
        {"question": "What is the capital of Spain?", "answers": ["Madrid"]},
        {"question": "Which planet is known as the Blue Planet?", "answers": ["Earth", "The Earth"]},
        {"question": "What is the fastest land animal?", "answers": ["Cheetah"]},
        {"question": "How many bones are there in the human body?", "answers": ["206"]},
        {"question": "Which country is home to the toucan?", "answers": ["Brazil"]},
        {"question": "What is the chemical symbol for silver?", "answers": ["Ag"]},
        {"question": "Who painted the Starry Night?", "answers": ["Vincent van Gogh", "Van Gogh"]},
        {"question": "What is the largest desert in the world?", "answers": ["Sahara Desert", "Sahara"]},
        {"question": "What is the capital of Russia?", "answers": ["Moscow"]},
        {"question": "Which element has the atomic number 79?", "answers": ["Gold"]},
        {"question": "What is the largest bird in the world?", "answers": ["Ostrich", "The Ostrich"]},
        {"question": "Who sang the song 'Bohemian Rhapsody'?", "answers": ["Queen", "Freddie Mercury", "Mercury"]},
        {"question": "What is the title of Michael Jackson's best-selling single?", "answers": ["Thriller"]},
        {"question": "Who wrote and performed the song 'Imagine'?", "answers": ["John Lennon", "Lennon"]},
        {"question": "Which artist released the hit song 'Shape of You'?", "answers": ["Ed Sheeran", "Sheeran"]},
    ]

    random.shuffle(questions)
    questions = questions[:5]  
    correct_answers = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game! Answer the following 5 questions correctly to win.")

    for i, q in enumerate(questions, start=1):
        if ask_question(q["question"], q["answers"]):
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answers are: {', '.join(q['answers'])}\n")

    print(f"Quiz completed! You got {correct_answers} out of {total_questions} questions correct.")

    if correct_answers == total_questions:
        print("Congratulations! You won the game!")
    else:
        print("Better luck next time. Try again!")

if __name__ == "__main__":
    play_quiz()
