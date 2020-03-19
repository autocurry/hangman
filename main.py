from words import wordlist
import random       

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

def start():
    try:
        temp = random.choice(wordlist)
        wordlist.remove(temp)     
        return temp
    except:
        return None

HANGED_MAN = {
        6: "     _______\n    |/      |\n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        5: "     _______\n    |/      |\n    |      (_)\n    |      \n    |       \n    |      \n    |\n____|________\n",
        4: "     _______\n    |/      |\n    |      (_)\n    |       |\n    |       |\n    |      \n    |\n____|________\n",
        3: "     _______\n    |/      |\n    |      (_)\n    |      \\|\n    |       |\n    |      \n    |\n____|________\n",
        2: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      \n    |\n____|________\n",
        1: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \n    |\n____|________\n",
        0: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \\\n    |\n____|________\n"
    }
