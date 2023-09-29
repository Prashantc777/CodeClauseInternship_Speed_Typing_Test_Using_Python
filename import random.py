import random
import time

def generate_random_word():
    words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "house", "igloo", "jacket"]
    return random.choice(words)

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    score = 0
    num_rounds = 5

    for _ in range(num_rounds):
        target_word = generate_random_word()
        print(f"Type the word: {target_word}")

        start_time = time.time()
        user_input = input()
        end_time = time.time()

        if user_input == target_word:
            elapsed_time = end_time - start_time
            score += 1
            print(f"Correct! Time taken: {elapsed_time:.2f} seconds")
        else:
            print("Incorrect. Try the next word.")

    print(f"Game Over! Your score: {score}/{num_rounds}")

if __name__ == "_main_":
    main()