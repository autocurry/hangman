import tkinter as tk
from tkinter import *
from main import *
import time
from tkinter import messagebox

score='some score'
balancetries = 6
logmessages = {
    6:"Welcome, You have 6 tries",
    5:"Don't worry, you \n have 5 more tries",
    4:"Be careful, you have \n 4 more tries",
    3:"Please don't kill me, \n only 3 tries left",
    2:"Common, think, use your \n brain, only 2 tries left",
    1:"Unbelivable,you are \n killing me. 1 try left",
    0:"I'm Dead, please do \n some reading."
}
alphabetsrow = [
        ['Q','W','E','R','T','Y','U','I','O','P'],
        ['A','S','D','F','G','H','J','K','L'],
        ['Z','X','C','V','B','N','M']
     ]

_start = time.time()     
_elapsedtime = 0.0
_timer = None
totalscore = len(wordlist)
correctanswer = 0


root=tk.Tk()
root.title("Save the - INVESTOMAN")

baseframe = tk.Frame(root,height=600,width=900)
baseframe.pack()

totalframe = tk.Frame(baseframe, bg='#ffffff')
totalframe.place(relx=0.5,rely=0,relwidth=0.85,relheight=0.1,anchor='n')

scorelabel = tk.Label(totalframe, text="  Total Score:  ",bg="white",fg="Black",font=('Helvetica','16'))
scorelabel.grid(column=0,row=0)

scorevalue = tk.Entry(totalframe,bg="skyBlue",fg="Black",font=('Helvetica','16'),width=6)
scorevalue.grid(column=3,row=0)

watchlabel = tk.Label(totalframe,text="  Time Elapsed:  ",bg="white",fg="Black",font=('Helvetica','16'))
watchlabel.grid(column=7,row=0)

watchvalue=tk.Entry(totalframe,bg="skyBlue",fg="Black",font=('Helvetica','16'),width=10)
watchvalue.grid(column=10,row=0)

frame = tk.Frame(baseframe, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.35, anchor='n')


challengeframe = tk.Frame(frame, bg='#ffffff')
challengeframe.place(relx=0.35, rely=0.05,relwidth=0.8, relheight=0.9, anchor='n')

challengeframe1 = tk.Frame(challengeframe,bg='#ffffff')
challengeframe1.place(relx=0.5, rely=0.2,relwidth=0.8, relheight=0.5, anchor='n')
clueframe=tk.Frame(challengeframe, bg='#000000')
clueframe.place(relx=0.5, rely=0.6,relwidth=0.8, relheight=0.7, anchor='n')

lower_frame = tk.Frame(baseframe, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.85, relheight=0.35, anchor='n')

hangmanframe = tk.Frame(frame)
hangmanframe.place(relx=0.95, rely=0.05,relwidth=0.5, relheight=0.9, anchor='n')
hangmanimageframe=tk.Frame(hangmanframe,bg='#ffffff')
hangmanimageframe.place(relx=0.4, rely=0.005,relwidth=0.7, relheight=0.8, anchor='n')
hangmanlogframe = tk.Frame(hangmanframe,bg='#ffffff')
hangmanlogframe.place(relx=0.475, rely=0.75,relwidth=0.85, relheight=0.5, anchor='n')

text = Text(hangmanimageframe)
text.pack()
logtext=Text(hangmanlogframe)
logtext.pack()
cluetext = Text(clueframe, borderwidth=15, relief=tk.FLAT,font=('Helvetica','18'))
cluetext.pack()
fullword = ''
inputword=''
guessedwords=[]
uniqueletterscount=0

def printtoScreen(resultingstring):
    for newButton in challengeframe1.grid_slaves():
        newButton.grid_forget()
    for letter in range(0, len(resultingstring)):
        newButton = Button(challengeframe1, fg="Black",text=resultingstring[letter], width=2,height=1, font=('Helvetica','14')) 
        newButton.grid(column=letter+1, row=1)
def displayHangMan(hangmanstate):   
    text.delete(1.0,END)
    text.insert(INSERT, HANGED_MAN[hangmanstate])
    text.pack()
def displayHangManLog(logmessage):
    logtext.delete(1.0,END)
    logtext.insert(INSERT,logmessage)
def Windupthegame():
    stopTimer()
    messagebox.showinfo("Game Over", f'You reached the end of Game \n Your total score is: {scorevalue.get()} \n Your time is: {watchvalue.get()}')
    
def startthegame():   
    global fullword
    global uniqueletterscount   
    global balancetries
    global totalscore
    global correctanswer
    scorevalue.delete(0,END)
    scorevalue.insert(0,f'{correctanswer} / {totalscore}')
    balancetries = 6     
    fullwordlist = start() 
    if(fullwordlist is None):
        Windupthegame()
        root.destroy()
    guessedwords.clear()
    fullword = fullwordlist[0].upper()
    clue = fullwordlist[1]    
    cluetext.delete(1.0,END)
    cluetext.insert(INSERT,clue)    
    uniqueletterscount = len(list(set(fullword)))
    word = resultstring(fullword,'',guessedwords)    
    text.insert(INSERT, HANGED_MAN[6])
    logtext.insert(INSERT,"Welcome, You have 6 tries")
    logtext.pack()
    #Initial data displays
    printtoScreen(word)
    displayHangMan(6)
    displayHangManLog(logmessages[6])
def startTimer(): 
    global _start
    global _elapsedtime
    global _timer    
    _elapsedtime = time.time() - _start
    minutes = int(_elapsedtime/60)
    seconds = int(_elapsedtime - minutes*60.0)
    hseconds = int((_elapsedtime - minutes*60.0 - seconds)*100)
    watchvalue.delete(0,END)
    watchvalue.insert(0,'%02d:%02d:%02d' % (minutes, seconds, hseconds))               
    _timer = watchvalue.after(50, startTimer)
def stopTimer():
    global _timer
    watchvalue.after_cancel(_timer)

def fill():  
    printtoScreen(resultstring(fullword,inputword,guessedwords))
    displayHangMan(balancetries) 
    displayHangManLog(logmessages[balancetries])  

def clicked(alphabet):       
    global balancetries    
    global inputword
    global fullword
    global guessedwords  
    global uniqueletterscount  
    global alphabetsrow    
    inputword = alphabet.upper()    
    if(inputword in fullword):
        if(inputword not in guessedwords):
            guessedwords.append(inputword)
    else:
        balancetries -= 1    
    fill()       
    if(balancetries ==0):                
        if (messagebox.askyesno("You Lose", "You lose !!, You want to try another one ?") == True):
            startthegame()
        else:           
            root.destroy()
    if(len(guessedwords)==uniqueletterscount):
        global correctanswer
        correctanswer += 1
        if (messagebox.askyesno("You Won","YAY You Won !!, You want to try another one ?") == True):
            startthegame()
        else:            
            root.destroy()


def createkeyboard():
    global alphabetsrow
    i = 0
    j = 0
    for row in alphabetsrow:
        for letter in row:
            buttonprint = Button(lower_frame,text=letter.upper(),bg="skyBlue",fg="Black",width=3,height=1,font=('Helvetica','20'),command= lambda t=letter: clicked(t))            
            buttonprint.grid(column=i,row=j)            
            i+=1
        j+=1
        i=j

createkeyboard()     

startTimer()       
startthegame()

root.mainloop()

