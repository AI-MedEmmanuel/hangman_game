#🔹 Block 1: Imports and Word Setup
import random
words = ["rhythm", "knight", "queue", "breeze", "psych", "gossip", "awkward", "receipt", "island", "muscle"]
word = random.choice(words)

# Create display with "_" for each letter
display = ["_"] * len(word)

# Set lives
lives = 6

#🔹 Block 2: Greeting
def greet():
    print("🎮 Welcome to Hangman!")
    print("Guess a word please.\n")
greet()

#🔹 Block 3: GAME LOOP
while "_" in display and lives > 0:
    print(" ".join(display))
    user_choice = str(input("Type a letter below \n"))

    # setting and flag
    found = False

    #looping with index
    for _ in range(len(word)):
        if word[_] == user_choice:
            display[_] = user_choice
            found = True
    if found == False:
        lives -= 1
        print(f"Your life = {lives}")

#🔹 Block 4: After Loop Ends  
if lives > 0 and "_" not in display:
    print("You win congratulations!🏆🏆🏆 ")
else:
    lives < 0 and "_" in display
    print("You loose 😢, game over") 
