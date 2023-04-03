import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for letter in chosen_word: 
  display.extend("_")

game_over = False

while game_over == False: 
  guess = input("Guess a letter: ").lower()

  for i in range(0, word_length):
    if chosen_word[i] == guess:
      display[i] = guess

  print(display)

  if "_" not in display: 
    game_over = True

print("You win!")