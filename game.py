import random

# name for my game with 5 turns and 5 letters
game_title = "Guess A Word"

#word bank as list
word_bank = []
"""
friend
cherry
mirror
carrot
cheese
baloon
"""

# open text file of word bank
fname = 'words.txt'
# open word bank file
try:
    with open(fname, 'r') as handle:
        word_bank = [line.strip() for line in handle if line.strip()]
except FileNotFoundError:
    print(f"File not found: {fname}")
except Exception as e:
    print(f"an error occurred: {(e)}")

    

# create variable for guessed word
# word_guess = random.randint(0, len(word_bank - 1)).lower()

word_guess = random.choice(word_bank).lower()


# initial game variables
misplaced_letters = []
incorrect_letters =[]
turns_made = 0

# welcoming message to player
print(f"Welcome to" , game_title)
# creating easy level or hard level
level = input("easy or hard Level: \n")
if level == "easy":
   max_turns = 6
else:
   max_turns = 3

print(f"There are only", len(word_bank), "letters in the words for this game")
print(f"You have", max_turns , "turns to guess a word correctly")



# game loop

while max_turns > turns_made:
    guess = input("What is your word guess? \n").lower()
    # set guess to lower caase
    
# two condition to be met after entry of guess
    if len(guess) != len(word_guess) or not guess.isalpha():
        print("Please enter 6 letters words")
    
        continue
#as index
    index = 0

    for w in guess:
        if w == word_guess[index]:
          print(w, end=" ")
          if w in misplaced_letters:
            misplaced_letters.remove(w)
        elif w in word_guess:
            if w not in misplaced_letters:
              misplaced_letters.append(w)
            print("_", end=" ")
        else:
          if w not in incorrect_letters:
           incorrect_letters.append(w)
          print("_", end=" ")
        index += 1
    # feedback to players on misplaced and incoreect letters
    print("\nmisplaced letters: ", misplaced_letters)
    print("\nincorrect letters: ", incorrect_letters)
    turns_made += 1
    
    #check if player hs won by guessing correct words
    if guess == word_guess:
       print("Congratulations, you win")
       break

    # check if player has lost
    if max_turns == turns_made:
        print("You lose, the word was", {word_guess})
        break
    # notify of turns left
    
    print(f"You have", max_turns - turns_made, " turns left")

    

