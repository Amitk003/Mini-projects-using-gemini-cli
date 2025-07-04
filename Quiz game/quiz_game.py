import json
import os

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    }
]

LEADERBOARD_FILE = "quiz_leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)

def display_leaderboard(leaderboard):
    print("\n--- Leaderboard ---")
    if not leaderboard:
        print("No scores yet.")
        return
    
    # Sort by score in descending order
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    for i, entry in enumerate(sorted_leaderboard):
        print(f"{i+1}. {entry['name']}: {entry['score']} points")
    print("-------------------\n")

def run_quiz():
    score = 0
    print("Welcome to The Quiz Game!")

    for i, q_data in enumerate(QUESTIONS):
        print(f"\nQuestion {i+1}: {q_data['question']}")
        for option in q_data['options']:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if user_answer == q_data['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q_data['answer']}.")
    
    print(f"\nQuiz finished! You scored {score} out of {len(QUESTIONS)}.")

    leaderboard = load_leaderboard()
    player_name = input("Enter your name for the leaderboard: ").strip()
    leaderboard.append({"name": player_name, "score": score})
    save_leaderboard(leaderboard)
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    run_quiz()
