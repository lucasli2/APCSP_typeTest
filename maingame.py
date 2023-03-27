#Typing Test!
##Pseudocode:

import os
import time
import random

def menu():
    ##Text Display Section
    print("#"*18," Type Test ","#"*19)
    print("#\t","Enter 0 for Game\t\t\t\t\t\t\t","#")
    print("#\t","Enter 1 for Instructions\t\t\t\t\t", "#")
    print("#\t","Enter 2 for Leaderboard\t\t\t\t\t", "#")
    print("#\t","Enter Q to Quit\t\t\t\t\t\t\t", "#")
    print("#" * 50)

    user_selection = (input("")).lower()

    if user_selection == '0':
        length  =   lengthSelect()
        wordbank    =   wordbank_select()
        text = generate_text(length, wordbank)
        #[elapsed_time, words_typed, accuracy * 100, wpm]
        dataReturn = main_game(text)


    elif user_selection == '1':
        instructions()
    elif user_selection == '2':
        leaderboard()
    elif user_selection == 'q':
        quitScreen()
    else:
        menu()

def lengthSelect():
    print("#"*10,"Length Selection:","#"*10)
    length = input("Select length of text (5, 10, 20, or 50): ")
    if length in ["5", "10", "20", "50"]:
        return int(length)
    else:
        print("Invalid input, please try again.")




def wordbank_select():
    difficulty = input("Select difficulty level (easy, medium, hard): ")
    if difficulty == "easy":
        return 1
    elif difficulty == "medium":
        return 2
    elif difficulty == "hard":
        return 3
    else:
        print("Invalid input, please try again.")


def instructions():
    os.system("clear")
    print("#"*14,"Instructions","#"*14)
    print("Type the generated text as fast and accurately as you can.")
    print("Your score will be based on your accuracy and words per minute (WPM).")
    print("#"*50)

def leaderboard():
    print("#"*15,"Leaderboard","#"*14)
    print("#"*50)

def quitScreen():
    os.system("clear")
    print("#"*50)
    print("Are you sure you want to exit?")
    print("Enter q again to confirm")
    print("Enter m to return to Menu")
    print("#"*50)
    user_selection = input("").lower()
    if user_selection == 'q':
        exit()
    elif user_selection == 'm':
        menu()

def generate_text(length, difficulty):
    word_bank = {
        1: ["apple", "banana", "pear", "orange", "grape"],
        2: ["cat", "dog", "bird", "fish", "rabbit"],
        3: ["computer", "algorithm", "programming", "database", "network"]
    }
    words = []
    for i in range(length):
        words.append(random.choice(word_bank[difficulty]))
    text = " ".join(words) + "."
    print("Generated text:")
    print(text)
    return text

def main_game(text):
    input("Press enter to start the game...")
    print(text)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    start_time = time.time()
    user_text = input("Type the generated text and press enter: ")


    end_time = time.time()
    elapsed_time = end_time - start_time

    UserSplitted = user_text.split()
    textSplitted = text.split()


    words_typed = len(UserSplitted)
    print(textSplitted)
    print(UserSplitted)
    pointsum = 0

    for i in range(words_typed):
        point = 1
        for j in range(len(textSplitted[i])):
            try:
                if textSplitted[i][j] == UserSplitted[i][j]:
                    point += 1
                    print("Add Point", i, j)
                else:
                    continue
            except IndexError:
                continue

        pointsum += point

    if len(user_text)>2:
        accuracy = (pointsum-1)/len(text)
    else:
        accuracy = 0;


    wpm = words_typed / elapsed_time * 60


    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Words typed: {}".format(words_typed))
    print("Accuracy: {:.2f}%".format(accuracy * 100))
    print("Words per minute: {:.2f}".format(wpm))

    return [elapsed_time, words_typed, accuracy*100, wpm];


def view_leaderboards():
    with open("leaderboard.txt", "r") as f:
        rankings = []
        for line in f:
            name, wpm, accuracy = line.strip().split(",")
            wpm = float(wpm)
            accuracy = float(accuracy)
            if accuracy >= 0.85:
                rankings.append((name, wpm, accuracy))
        rankings.sort(key=lambda x: (x[1], x[2]), reverse=True)
        print("Leaderboards:")
        for i, (name, wpm, accuracy) in enumerate(rankings):
            print("{}. {}: {:.2f} WPM, {:.2f}% accuracy".format(i+1, name, wpm, accuracy))


#main_game("the quick brown fox jumped over the lazy dog")
menu()
