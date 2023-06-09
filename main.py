import random
import hangman_words
import hangman_art
import os

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
from hangman_art import logo, stages
print(logo)

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

display = []

for letter in chosen_word: 
  display.extend("_")

game_over = False

while game_over == False: 
  guess = input("Guess a letter: ").lower()

  clear_screen()

  if guess in display: 
    print("You've already successfully guessed this letter already")

  guess_successful = False
  
  for i in range(0, word_length):
    if chosen_word[i] == guess:
      display[i] = guess
      guess_successful = True

  if guess_successful == False:
    lives -= 1
    
    if lives != 0:
      print(f"Guess again! You have {lives} lives left \n")
    elif lives == 0: 
      print("You lose!")
      print(f"The answer was {chosen_word}")
      game_over = True
  elif guess_successful == True: 
    print("Keep going!")
  
  print(stages[lives])
  print(f"{' '.join(display)}")

  if "_" not in display: 
    game_over = True
    print("You win!")