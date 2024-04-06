import random
words = ['cheese', 'University', 'peppermint', 'icebreakers', 'notebook', 'tennis', 'tennessee','monkey']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
e_attempts = 10
m_attempts = 8
h_attempts = 6
print("Welcome to hangman, What difficulty would you like?\n 1). Easy\n 2)/ Medium\n 3). Hard\n")
j = 0
while j != 1:
    dif = input("Please enter E, M, or H: ").upper()  
    if dif == 'E':
        attempts = e_attempts
        j = 1
    elif dif == 'M':
        attempts = m_attempts
        j = 1
    elif dif == 'H':
        attempts = h_attempts  
        j = 1
    else:
        print("Please enter a valid number ")

while attempts >0 and '_' in word_display:
    print("\n" + ' '.join(word_display)) 
    guess = input("Please guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter does not appear in that word: ")
        attempts -= 1 

if '_' not in word_display:
    print("You guessed the right word! ")
    print('_'.join(word_display))
    print("You survived ")
else:
    print("You ran out of attempts " + chosen_word)
    print("You lost ")