Project Title - Creating Hangman Game on Python

Project Manager - Manav Gupta

Developer - Mridul 

Tester - Pranav Goyal


Project Manager-

Step 1-
    Word Selection: Use Random module to select a word but keeps it secret from the other players. The word should be of a reasonable length and not too difficult to guess, especially if playing with younger children.

Step 2-
    Display of Placeholder Letters: The program should print a series of dashes. This represents the unknown letters of the word.

Step 3-
    Guessing Mechanism: The other players (guessers) take turns guessing letters of the word. They can guess one letter at a time, and typically, guessing non-alphabetic characters or more than one letter at a time is not allowed.

Step 4-
    Revealing Correct Guesses: If a guesser correctly guesses a letter in the word, the program should replace the letter in the corresponding blank space(s) of the word. If the letter appears multiple times in the word, all instances of it should be revealed.

Step 5-
    Revealing Incorrect Guesses: If a guesser guesses a letter that is not in the word, the program prints parts of a gallows and hangman. Each incorrect guess results in the addition of another body part to the gallows and the hangman (e.g., head, body, arms, legs). Once the entire hangman is drawn (typically six incorrect guesses), the game ends.

Step 6-
    End Conditions: The game ends when either:
      > The guessers correctly guess all the letters in the word, in which case they win.
      > The hangman is completely printed, indicating that the guessers have run out of guesses, in which case they lose.

Step 7-
    Outcome Display: Once the game ends, the program reveals the entire word to the guessers. If they successfully guessed all the letters, the program congratulates them on their win. If the hangman is complete, the program reveals the word and commiserates with the guessers on their loss.
Step 8-
    Play Again: Players can choose to play again and the program selects a new word.



Developer-

The code as requested has been developed and pushed on Github. All the requsted features have been added.


Tester-

There are some bugs in the code which the developer should resolve.

    1. The code is not working if words with repeating letters are chosen.
    
    2. There is no option to play again.

Developer-
The bugs given by tester have been resolved and code has been pushed .


Tester-

There are some more bugs in code which the developer should resolve.

    1. The code is not working properly if the input is digit.
    
    2. The code is not working properly if the input is string of length greater than one .

Developer-

The given errors has been resolved and the code is working properly . 


Tester-

The program is now working properly and is ready for final release.
 

 Project Manager -

 The program is working properly. The developer should now make a GUI for it and prepare the program for the final release.

Developer-

The final code of game with integrated GUI has been pushed 


