from words import wordlist
import random

message ='please enter a letter'

def main():
    tries = 6
    tried =0
    guessedwords=[]
    fullword = start()   
    uniquelength = len(set(fullword))
    finalmessage='Game Over, Do you want to play again'
    while(tried < tries) :      
        print(' ')
        print(message)
        inputword = str(input()).upper()
        #print('word entered is',inputword)        
        if(inputword in fullword) :
            print("Great!, you entered a correct letter")  
            if (inputword not in guessedwords):
                guessedwords.append(inputword)       
        else:
            tried += 1
            print(f'You entered a wrong word, you have {tries-tried} more tries remaining')
        print(resultstring(fullword,inputword,guessedwords))           
        if(len(guessedwords) == uniquelength-1):
            finalmessage = 'YAY!, you won. Do you want to play again'            
            break    
        print(HANGED_MAN[tried])     
    #print(HANGED_MAN[6])   
    print(finalmessage)
    option=input().upper()
    if(option == 'Y'):
        main()
    else:
        print('Thanks for Playing Hangman, see you later')
        

def resultstring(onefullword,oneinputword,oneguessedwords):
    resultfull={}
    if(len(oneguessedwords)==0):
        for item in range(0,len(onefullword)):
            resultfull[item]=' '
        return resultfull
    else:
        for item in range(0, len(onefullword)):
            if(onefullword[item] in oneguessedwords):
                resultfull[item] = onefullword[item]
            elif (onefullword[item] in oneinputword):
                resultfull[item] = onefullword[item]
            else:
                resultfull[item] = ' '
        return resultfull


            
    #for eachword in onefullword:
        #if(eachword != ' '):
            #if(oneinputword in eachword):
                #print(eachword, end =" ")
            #elif (eachword in oneguessedwords):
                #print(eachword, end =" ")
            #else:
                #print('_', end =" ")
        #print(' ', end =" ")

def start():
    temp = random.choice(wordlist)
    wordlist.remove(temp)
    word = temp.upper()    
    print(HANGED_MAN[0])
    #print(word)
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
