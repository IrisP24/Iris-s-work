#hangman project: https://codefather.tech/blog/hangman-game-python/
import random
import hangman_stages #so we can generate a random number and import the hangman_stages file
import sys

def create_animal_list():
    with open("animals.txt","r") as animals_file: #with as is more concise
        animal_words = animals_file.read()
        animal_list = animal_words.split()
    return animal_list

def create_name_list():
    with open("names.txt", "r") as name_file:
        name_words = name_file.read()
        name_list = name_words.split()
    return name_list #return means you can use the lists in the global scope - I think??


def select_word(retrieval_list):
    return random.choice(retrieval_list)
#this function (declared by def) uses random.choice() to return a random element from a sequence.
#this function works the same as those in js
#print(select_word(words)) checks that the select_word function works - it does!


remaining_attempts = 6 #how many more incorrect guesses do you have
guessed_letters = "" #will store the letters that the user has guessed

mode = int(input("Welcome to Hangman! Choose a mode. Press 1 for animal, 2 for names. ")) #remember that these should be integers (originally used them as strings so logic didn't work)
if mode == 1:
    topic = "animal"
    animal_list = create_animal_list() #means that lists can be accessed in the global scope rather than local scope in the functions
    secret_word = select_word(animal_list)
elif mode == 2:
    topic = "name"
    name_list = create_name_list() #same as above
    secret_word = select_word(name_list)
else:
    print("Try again. Something has gone wrong. ")
    sys.exit()
secret_word = secret_word.lower()


print("Okay, let's go! Let's see if you can guess the {}.".format(topic))
print(secret_word)

def print_secret_word(secret_word, guessed_letters):
    for letter2 in secret_word:
        if letter2 in guessed_letters:
            print(" {} ".format(letter2), end="")
        else:
            print(" _ ", end="")
    print("\n")

def is_guess_in_secret_word(letter, secret_word):
    if letter.isalpha() and len(letter) == 1:
            if letter in secret_word:
                return True
            else:
                return False
    else:
        print("Only single letters are allowed. ")
        sys.exit()

# ^ calls the function select_word() to choose a random word and assigns it to a variable
unique_letters_in_word = "".join(set(secret_word)) #this turns secret_word into a set, which doesn't allow duplicate letters so you know how many unique letters are in secret_word

while remaining_attempts > 0 and len(guessed_letters) < len(unique_letters_in_word): #repeats while you have lives left and you have letters left to guess
    print(hangman_stages.get_hangman_stage(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    # ^ prints underscores for the number of letters in the word by calling print_secret_word() function
    letter = input("What is your guess? Remember: no multiple letters, no numbers, no other characters. ")
    guess_in_secret_word = is_guess_in_secret_word(letter, secret_word)

    if guess_in_secret_word: #guess_in_secret_word is a boolean from the function is_guess_in_secret_word
        if letter in guessed_letters: #checks if letter is in previous array for guessed letter
            print("You have already guessed the letter {}".format(letter)) #uses string manipulation to insert the letter that you have previously guessed
        else:
            print("Yes! The letter '{}' is part of the secret word".format(letter))
            guessed_letters += letter
    else:
        print("No! The letter {} is not part of the secret word".format(letter))
        remaining_attempts -= 1
if remaining_attempts == 0:
    print("Sorry, you have run out of lives. Please try again. ")
if len(guessed_letters) == len(unique_letters_in_word):
    print("------------------------------------------------------")
    print("Yay, you won!!")
    print("You had {} remaining lives".format(remaining_attempts))
    print( "The word was {}".format(secret_word))
else:
    print("Sorry, something went wrong. Try again")
