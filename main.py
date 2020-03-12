from words import wordlist
import random

message ='please enter a letter'
tried =0

def main():
    tries = 6
    fullword = start()
    inputword = str(input()).upper()
    print('word entered is',inputword)
    while tries > 0 :
        tries -= 1
        if(inputword in fullword) :
            print("Great!, you entered a correct letter")
            for eachword in fullword:
                print('_ '*len(eachword), end =" ")

def start():
    word = random.choice(wordlist).upper()
    wordtolist = word.split(' ')
    print("welcome to handman game")
    for eachword in wordtolist:
        print('_ '*len(eachword), end =" ")
    print(' ')
    print(HANGED_MAN[0])
    print(' ')
    print(message)
    return word

HANGED_MAN = {
        0: "     _______\n    |/      |\n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        1: "     _______\n    |/      |\n    |      (_)\n    |      \n    |       \n    |      \n    |\n____|________\n",
        2: "     _______\n    |/      |\n    |      (_)\n    |       |\n    |       |\n    |      \n    |\n____|________\n",
        3: "     _______\n    |/      |\n    |      (_)\n    |      \\|\n    |       |\n    |      \n    |\n____|________\n",
        4: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      \n    |\n____|________\n",
        5: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \n    |\n____|________\n",
        6: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \\\n    |\n____|________\n"
    }

if __name__=="__main__":
    main()