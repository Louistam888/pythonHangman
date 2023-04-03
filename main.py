import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
guess = input("Guess a letter: ").lower()

for letter in chosen_word: 
  display.extend("_")

for i in range(0, len(chosen_word)):
  if chosen_word[i] == guess:
    display[i] = guess

print(display)