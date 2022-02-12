# Copyright © 2021 by Andre Lustosa. All rights reserved.
# Licensed under the Creative Commons Attribution 4.0 International License.
# See LICENSE in the project root for license information.


"""Wordle Solver

This script allows you to solve wordle puzzles.

Usage:  python wordle_solver.py  <words_file>

This script requires a dataset of all words acceptable by wordle

This file cannot be imported, it must be run as a script.
"""

import operator
import os
import sys

def main():
    """Main 

    Parameters:
        None
    Returns:
        None

    """
    # Initialize state variables
    contained_letters = []
    excluded_letters = []
    position_letters = []
    notposition_letters = []

    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage:  python wordle_solver.py <words_file>")
        sys.exit(1)

    # Get the words file
    dictionary_file = sys.argv[1]


    with open(dictionary_file,'r') as file:
        words = file.readlines()

    WORD_LEN = len(words[0])

    def startingGuess():
        if 'words.txt' in dictionary_file:
            print("STARTING GUESS = ALERT")
        if 'palavras.txt' in dictionary_file:
            print("STARTING GUESS = AIOES")	

    startingGuess()
    # Print the avaiable commands
    print("Available commands:")
    print("\ta <letter> <position> - informs a letter is part of the word and is in the correct position")
    print("\ta <letter> n <position> - informs a letter is part of the word and is NOT in the correct position")
    print("\tr <letter> - informs a letter is not part of the word")
    print("\tu <a/r> <letter> - undoes the informed command. Positional variables are also undone")
    print("\tp - processes the current state of the puzzle and prints the current suggestions")
    print("\tc - clears the console window")
    print("\t? - prints this list of commands")
    print("\tx - resets the program to its initial state")
    print("\tq - quits the program")
    print("\nSpaces are ignored in the commands, feel free to not use them once you are familiar with them\n")

    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


    while(1):
        command = "".join(input("Enter a command: ").split())
        if command == "" or command == " " or command == None:
            continue
        
        # Help command
        elif command[0] == "?":
            print("Available commands:")
            print("\ta <letter> <position> - informs a letter is part of the word and is in the correct position")
            print("\ta <letter> n <position> - informs a letter is part of the word and is NOT in the correct position")
            print("\tr <letter> - informs a letter is not part of the word")
            print("\tu <a/r> <letter> - undoes the informed command. Positional variables are also undone")
            print("\tp - processes the current state of the puzzle and prints the current suggestions")
            print("\tc - clears the console window")
            print("\t? - prints this list of commands")
            print("\tx - resets the program to its initial state")
            print("\tq - quits the program")
            print("\nSpaces are ignored in the commands, feel free to not use them once you are familiar with them\n")

        # Restart command
        elif command[0] == "x":
            contained_letters = []
            excluded_letters = []
            position_letters = []
            notposition_letters = []
            startingGuess()
            continue

        # Clear command
        elif command[0] == "c":
            clear()

        # Quit command
        elif command[0] == "q":
            break

        # Add letter command
        elif command[0] == "a":
            letter = command[1]
            
            if letter not in contained_letters:
                contained_letters.append(letter)
            
            if (len(command) > 2 ):
                if command[2] == "n":
                    position = int(command[3]) - 1
                    if (letter, position)  not in notposition_letters:
                        notposition_letters.append((letter,position))
                else:
                    position = int(command[2]) - 1
                    if (letter, position) not in position_letters:
                        position_letters.append((letter,position))
                continue

        # Remove letter command
        elif command[0] == "r":
            letter = command[1]
            if letter not in excluded_letters:
                excluded_letters.append(letter)
            continue

        # Undo operation command
        elif command[0] == "u":
            if command[1] == "a":
                letter = command[2]
                contained_letters = [x for x in contained_letters if x != letter]

                for i in range(len(position_letters)):
                    if position_letters[i][0] == letter:
                        position_letters.remove(position_letters[i])
                        break
                for i in range(len(notposition_letters)):
                    if notposition_letters[i][0] == letter:
                        notposition_letters.remove(notposition_letters[i])
                        break
                continue
            
            if command[1] == "r":
                letter = command[2]
                excluded_letters = [x for x in excluded_letters if x != letter]
                continue

        # Process state and print command
        elif command == "p":
        
            # Get the words that match the current state
            filtered_words = [word for word in words if all([letter in word for letter in contained_letters])]
            filtered_words = [word for word in filtered_words if not any([letter in word for letter in excluded_letters])]
            for letter, position in position_letters:
                filtered_words = [word for word in filtered_words if word[position] == letter]
            for letter, position in notposition_letters:
                filtered_words = [word for word in filtered_words if word[position] != letter]

            # Print the current state
            print("Excluded:", excluded_letters)
            print("Contained:", contained_letters)

            # Print the current known letters
            print("What we know:", end=" ")
            for i in range(WORD_LEN):
                if i in [x[1] for x in position_letters]:
                    print(next(x[0] for x in position_letters if x[1] == i), end="")
                else:
                    print("?", end="")
            print()

            # Print the number of words that match the current state
            print("There are", len(filtered_words), "possible words")
            
            # Calculate the frequency of each letter in the surviving words
            entropy = {}
            letters = [x for x in "abcdefghijklmnopqrstuvwxyz" if x not in excluded_letters and x not in contained_letters]
            
            for letter in letters:
                entropy[letter] = 0
                
            for word in filtered_words:
                for letter in word:
                    if letter in entropy:
                        entropy[letter] += 1

            
            # Print remaining letters in descending order of frequency
            print("Remaining letters:", end=" ")
            for letter in sorted(entropy, key=entropy.get, reverse=True):
                print(letter, end=", ")
            print()

            # Using the frequency of each letter
            # Calculate an entropy score for each word that matches the current state
            # Normalize the entropy score by the number of words
            # Only take into account unique letters in the word
            entropy_words = {}
            for word in filtered_words:
                entropy_words[word] = 0
            for word in filtered_words:
                seen = set()
                for letter in word:
                    if letter in entropy and letter not in seen:
                        entropy_words[word] += entropy[letter]
                        seen.add(letter)
            for word in filtered_words:
                entropy_words[word] = entropy_words[word] / len(filtered_words)

    
            # Sort the words by their entropy score
            sorted_words = sorted(entropy_words.items(), key=operator.itemgetter(1), reverse=True)
            

            # If there are no words that match the current state, the puzzle is solved
            # Print the solution and reset the program
            if len(sorted_words) == 1:
                print("There is only one possible word you won!")
                print("SOLUTION:", sorted_words[0][0])
                contained_letters = []
                excluded_letters = []
                position_letters = []
                notposition_letters = []

                startingGuess()

            # If there are multiple words that match the current state
            # Print the suggestions in descending order of entropy score
            else:
                # Print the entropy scores in scientific notation
                print("Suggestions:")
                for word, entropy in sorted_words:
                    print(word.strip(), ":", "{:.2e}".format(entropy), end=" ")
                print()
        # Invalid command
        else:
            print("Invalid command")
            continue

# Run the program
if __name__ == "__main__":
    main()