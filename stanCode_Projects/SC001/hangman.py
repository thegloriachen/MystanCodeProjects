"""
File: hangman.py
Name: Gloria
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users see a dashed word, trying to correctly figure the un-dashed word out by inputting one character each round.
    If the user input is correct, show the updated word on console.
    """
    ans = random_word()
    dashed_ans = dash_ans(ans)
    print("The word look like: " + dashed_ans)
    print("You have " + str(N_TURNS) +" wrong guesses left.")
    chances = N_TURNS
    while True:
        guess = str(input("You guess: "))
        # while loop判斷是否有不屬於alpha或字元大於1的input
        while not guess.isalpha() or len(guess) > 1:
            print("Illegal format.")
            guess = str(input("Your guess: "))
        # 若input為小寫字母則轉換為大寫
        if guess.islower():
            guess = guess.upper()
        guess_ans = ""
        # 先判斷此次input是否有猜中
        if ans.find(guess) != -1:
            print("You are correct!")
            for i in range(len(ans)):
                ch = ans[i]
                if guess == ch:
                    guess_ans += guess
                else:
                    guess_ans += dashed_ans[i]
            dashed_ans = guess_ans
        else:
            print("There is no " + guess + "\'s in the world.")
            chances -= 1
        # 若已全部猜中則break
        if dashed_ans == ans:
            print("You win!!")
            print("The answer is: " + str(dashed_ans))
            break
        # 若機會用完則break
        if chances == 0:
            print("You are completely hung :(")
            break
        print("You have " + str(chances) +" wrong guesses left.")
        print("The word look like: " + dashed_ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dash_ans(ans):
    """
    param: the random answer to be dashed
    """
    dash = ""
    for i in range(len(ans)):
        dash += "-"
    return dash

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
