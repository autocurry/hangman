from words import wordlist
import random

message ='please enter a letter'

def main():
    tries = 6
    tried =0
    fullword = start()    
    while(tried < tries) :
        inputword = str(input()).upper()
        print('word entered is',inputword)
        tried += 1
        if(inputword in fullword) :
            print("Great!, you entered a correct letter")            
        else:
            print(f'You entered a wrong word, you have {tries} more tries remaining')
        print(resultstring(fullword,inputword))
        print(HANGED_MAN[tried])
        print(' ')
        print(message)
    print(HANGED_MAN[6])   
        

def resultstring(onefullword,oneinputword):
    for eachword in onefullword:
        if(eachword != ' '):
            if(oneinputword in eachword):
                print(oneinputword, end =" ")
            else:
                print('_', end =" ")

def start():
    word = random.choice(wordlist).upper()
    wordtolist = word.split(' ')
    print("welcome to hangman game")
    for eachword in wordtolist:
        print('_ '*len(eachword), end =" ")
    print(' ')
    print(HANGED_MAN[0])
    print(' ')
    print(message)
    print(word)
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