import random

words = ["banana", "apple", "cherry", "tomato", "mango", "orange", "watermelon", "sugarcane", "pawpaw"]

random_word = random.choice(words)
print(random_word)

letter_list = list(random_word)
guessed_letters = []
chances = len(letter_list) + 2

while chances > 0:
    guess = input("Guess the word! HINT: word is a name of a fruit, TYPE IN A LETTER: ")

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(guess)

    if guess not in letter_list:
        chances -= 1
        print("Wrong guess, chances left.", chances)
    else:
        print("Good guess")

    display = ""
    for letter in letter_list:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("🎉 You won!")
        break

if chances == 0:
    print("😢 You lost! The word was:", random_word)