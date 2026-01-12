

import random

words = [ "pasta", "pizza", "mouse", "gamer", "razor"]
secret_word = random.choice(words)
attempts = 6

print(" Welcome to Wordle! ")
print(" Guess the word. You have six tries.")

for attempt in range(1, attempts + 1):
    guess = input(f"Attempt {attempt}/6: ").lower()
    if len(guess) != 5:
        print("Please enter a 5 character long word")
        continue