import random

def word_display(word_bank, guessed_letters):

    return ''.join(letter if letter in guessed_letters else '-' for letter in word_bank)


def main ():
    word_bank = ['moustache', 'water', 'charge']
    word_choice = random.choice(word_bank).lower() 
    guessed_letters = []
    strikes = 0
    max_strikes = 5
    

    print('Welcome to hangman! Guess the word:', word_display(word_choice, guessed_letters))

    while strikes < max_strikes:

        guess = str(input("Please guess a letter or type quit to exit: ").lower()) #convert inputs to lowercase
        
        if guess == 'quit':
            break
        
        elif guess in word_choice:
            guessed_letters.append(guess)
            print("Good guess! Keep going", word_display(word_choice, guessed_letters))
            print(guessed_letters)

            if all(letter in guessed_letters for letter in word_choice):
                print("You win! Nice job.")
                break

        elif guess not in word_choice:
            guessed_letters.append(guess)
            strikes += 1
            strikes_left = max_strikes - strikes
            print(f"Nope. Try again: {strikes_left}")
            print(guessed_letters)

        elif guess in guessed_letters:
            print("Letter already guessed! Try again.")
            print(guessed_letters)
        
            

    else:
        print(f"You've ran out of strikes. Game over! The word was {word_choice}")
        
main()

