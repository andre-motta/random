import operator
import os

contained_letters = []
excluded_letters = []
position_letters = []
notposition_letters = []
print("STARTING GUESS = ALERT")

with open('words.txt','r') as file:
    words = file.readlines()


while(1):
    command = "".join(input("Enter a command: ").split())
    if command == "" or command == " " or command == None:
        continue
    
    # Restart
    if command[0] == "x":
        contained_letters = []
        excluded_letters = []
        position_letters = []
        notposition_letters = []
        print("STARTING GUESS = ALERT")
        continue

    # Clear
    if command == "c":
        clear = lambda: os.system('cls')
        clear()

    # Quit
    if command == "q":
        break

    # Add letter
    if command[0] == "a":
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

    # Remove letter
    if command[0] == "r":
        letter = command[1]
        if letter not in excluded_letters:
            excluded_letters.append(letter)
        continue

    # Undo Operation
    if command[0] == "u":
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

    # Print
    if command == "p":
        
        filtered_words = [word for word in words if all([letter in word for letter in contained_letters])]
        
        filtered_words = [word for word in filtered_words if not any([letter in word for letter in excluded_letters])]
        
        for letter, position in position_letters:
            filtered_words = [word for word in filtered_words if word[position] == letter]
        
        for letter, position in notposition_letters:
            filtered_words = [word for word in filtered_words if word[position] != letter]

        print("Excluded:", excluded_letters)
        print("Contained:", contained_letters)

        print("What we know:", end=" ")
        for i in range(5):
            if i in [x[1] for x in position_letters]:
                print(next(x[0] for x in position_letters if x[1] == i), end="")
            else:
                print("?", end="")
        print()

        print("There are", len(filtered_words), "possible words")
        
        # calculate the entropy of each letter in the filtered words normalized by the number of letters in the filtered words
        entropy = {}
        letters = [x for x in "abcdefghijklmnopqrstuvwxyz" if x not in excluded_letters and x not in contained_letters]
        
        for letter in letters:
            entropy[letter] = 0
            
        for word in filtered_words:
            for letter in word:
                if letter in entropy:
                    entropy[letter] += 1

        
        # print remaining letters in descending order of entropy
        print("Remaining letters:", end=" ")
        for letter in sorted(entropy, key=entropy.get, reverse=True):
            print(letter, end=", ")
        print()

        # calculate the entropy of each word from letter entropy normalized by the number of words in the filtered words
        # double letters are not counted twice
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



       

        
        # sort the words by entropy in descending order
        sorted_words = sorted(entropy_words.items(), key=operator.itemgetter(1), reverse=True)
        # print all the words and their entropy
        # print the entropy with scientific notation
        print("Entropy:")
        for word, entropy in sorted_words:
            print(word.strip(), ":", "{:.2e}".format(entropy), end=" ")
        print()

        if len(sorted_words) == 1:
            print("There is only one possible word you won!")
            contained_letters = []
            excluded_letters = []
            position_letters = []
            notposition_letters = []

            print("STARTING GUESS = ALERT")