from tkinter import *
from string import ascii_uppercase
import random

def guessfun():
    win = Tk()
    win.iconbitmap("stick-man.ico")
    win.minsize(width=1300, height=600)
    win.title("Hangman Game")

    words = [
        "apple", "apricot", "avocado", "banana", "blackberry", "blueberry",
        "carrot", "cherry", "coconut", "corn", "cucumber",
        "date", "eggplant", "fig", "grape", "grapefruit", "green bean",
        "kiwi", "lemon", "lettuce", "lime", "mango", "nectarine", "onion",
        "orange", "papaya", "peach", "pear", "peas", "pineapple", "plum",
        "pomegranate", "potato", "pumpkin", "raspberry",
        "spinach", "squash", "strawberry", "tomato", "watermelon", "pizza", "burger",
        "chips", "juice", "bread", "puff", "fries", "tacos", "biscuits", "paratha", "paneer",
        "chaap", "kebab", "pasta", "macroni", "sphagetti", "maggi", "noodles"
    ]
    pictures = [PhotoImage(file="hang5.png"), PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"),
                PhotoImage(file="hang8.png"), PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"),
                PhotoImage(file="hang11.png")]

    def display_word(word, guesses):
        word = word.upper()
        return ' '.join(letter if letter.upper() in guesses else '_' for letter in word)

    def update_image():
        nonlocal wrong_guesses
        if wrong_guesses < len(pictures):
            hangman_image.config(image=pictures[wrong_guesses])

    def check_letter(letter):
        nonlocal wrong_guesses, word_to_guess, guessed_letters, correct_guesses, message
        if letter in guessed_letters:
            message.set("You have already guessed this letter.")
            return

        guessed_letters.add(letter)  # Add the guessed letter to guessed letters

        if letter in word_to_guess:
            correct_guesses.set(display_word(word_to_guess, guessed_letters))
            if '_' not in correct_guesses.get():
                message.set("Congratulations!! You Won")
        else:
            wrong_guesses += 1
            update_image()
            if wrong_guesses >= len(pictures):
                message.set("You ran out of chances. The correct word was " + word_to_guess)
            else:
                # Filter out correct guesses before displaying wrong guesses
                wrong_guess_list = [ltr for ltr in guessed_letters if ltr not in word_to_guess]
                message.set("Wrong Guesses: " + ' '.join(sorted(wrong_guess_list)))

    def reset_game():
        nonlocal word_to_guess, guessed_letters, wrong_guesses
        word_to_guess = random.choice(words).upper()
        guessed_letters.clear()
        correct_guesses.set(display_word(word_to_guess, guessed_letters))
        wrong_guesses = 0
        update_image()
        message.set("")

    word_to_guess = random.choice(words).upper()  # Convert word to uppercase
    guessed_letters = set()
    wrong_guesses = 0 

    top_frame = Frame(win, bg="steelblue")
    top_frame.grid(row=0, column=0, columnspan=25, sticky="ew")

    label = Label(top_frame, text="Can you save your Hangman ?", font=("Arial", 25), bg="steelblue", fg="Black", padx=20)
    label.grid(row=0, column=2, sticky="ew")

    hangman_image = Label(top_frame, bg="steelblue")
    hangman_image.config(image=pictures[0])
    hangman_image.grid(row=1, column=0, rowspan=2, columnspan=3, padx=10, pady=156)

    correct_guesses = StringVar()
    correct_guesses.set(display_word(word_to_guess, guessed_letters))
    guess_label = Label(top_frame, textvariable=correct_guesses, font=("Arial", 20), bg="steelblue", fg="Black")
    guess_label.grid(row=1, column=24, sticky="e")

    message = StringVar()
    message_label = Label(top_frame, textvariable=message, font=("Arial", 15), bg="steelblue", fg="Black")
    message_label.grid(row=2, column=24, sticky="e")

    keyboard_frame = Frame(win)
    keyboard_frame.grid(row=2, column=0, columnspan=18, sticky="ew")

    for i, c in enumerate(ascii_uppercase):
        row = i // 9
        column = i % 9
        Button(keyboard_frame, text=c, height=4, width=20, pady=10, bg="lightgrey", fg="red", bd=3,
               command=lambda letter=c: check_letter(letter)).grid(row=row, column=column)

    Button(keyboard_frame, text="New Game", height=4, width=20, bg="lightgrey", fg="red", pady=10,
           command=reset_game).grid(row=row, column=column + 1)

    win.mainloop()

guessfun()
