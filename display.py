import tkinter as tk
from tkinter import *
from main import *
import time
from tkinter import messagebox

balancetries = 6
logmessages = {
    6:"Welcome, You have 6 tries",
    5:"Don't worry, you have 5 more tries",
    4:"Be careful, you have 4 more tries",
    3:"Please don't kill me, only 3 tries left",
    2:"Common, think, use your brain, only 2 tries left",
    1:"Un Belivable, you are killing me? only 1 try left",
    0:"I'm Dead, please do some reading."
}


root=tk.Tk()
root.title("Save the - INVESTOMAN")

baseframe = tk.Frame(root,height=600,width=900)
baseframe.pack()

frame = tk.Frame(baseframe, bg='#80c1ff', bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.35, anchor='n')

challengeframe = tk.Frame(frame, bg='#ffffff')
challengeframe.place(relx=0.35, rely=0.05,relwidth=0.8, relheight=0.9, anchor='n')

challengeframe1 = tk.Frame(challengeframe,bg='#ffffff')
challengeframe1.place(relx=0.5, rely=0.3,relwidth=0.8, relheight=0.6, anchor='n')
lower_frame = tk.Frame(baseframe, bg='#80c1ff', bd=3)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.85, relheight=0.35, anchor='n')

hangmanframe = tk.Frame(frame)
hangmanframe.place(relx=0.95, rely=0.05,relwidth=0.5, relheight=0.9, anchor='n')
hangmanimageframe=tk.Frame(hangmanframe,bg='#ffffff')
hangmanimageframe.place(relx=0.4, rely=0.005,relwidth=0.7, relheight=0.8, anchor='n')
hangmanlogframe = tk.Frame(hangmanframe,bg='#ffffff')
hangmanlogframe.place(relx=0.4, rely=0.85,relwidth=0.7, relheight=0.2, anchor='n')


btn1 = Button(lower_frame, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
btn1.grid(column=1, row=1)
btn2 = Button(lower_frame, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn2.grid(column=2, row=1)
btn3 = Button(lower_frame, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn3.grid(column=3, row=1)
btn4 = Button(lower_frame, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn4.grid(column=4, row=1)
btn5 = Button(lower_frame, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn5.grid(column=5, row=1)
btn6 = Button(lower_frame, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn6.grid(column=6, row=1)
btn7 = Button(lower_frame, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn7.grid(column=7, row=1)
btn8 = Button(lower_frame, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn8.grid(column=8, row=1)
btn9 = Button(lower_frame, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn9.grid(column=9, row=1)
btn10 = Button(lower_frame, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn10.grid(column=10, row=1)

btn11 = Button(lower_frame, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn11.grid(column=2, row=2)
btn12 = Button(lower_frame, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn12.grid(column=3, row=2)
btn13= Button(lower_frame, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn13.grid(column=4, row=2)
btn14 = Button(lower_frame, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn14.grid(column=5, row=2)
btn15 = Button(lower_frame, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
btn15.grid(column=6, row=2)
btn16 = Button(lower_frame, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn16.grid(column=7, row=2)
btn17 = Button(lower_frame, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
btn17.grid(column=8, row=2)
btn18 = Button(lower_frame, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
btn18.grid(column=9, row=2)
btn19 = Button(lower_frame, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn19.grid(column=10, row=2)

btn31 = Button(lower_frame, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn31.grid(column=3, row=3)
btn32 = Button(lower_frame, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn32.grid(column=4, row=3)
btn33 = Button(lower_frame, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn33.grid(column=5, row=3)
btn34 = Button(lower_frame, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn34.grid(column=6, row=3)
btn35 = Button(lower_frame, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn35.grid(column=7, row=3)
btn36 = Button(lower_frame, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn36.grid(column=8, row=3)
btn37 = Button(lower_frame, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn37.grid(column=9, row=3)
text = Text(hangmanimageframe)
text.pack()
logtext=Text(hangmanlogframe)
logtext.pack()
fullword = ''
inputword=''
guessedwords=[]



def printtoScreen(resultingstring):
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
    
def startthegame():   
    global fullword
    fullword = start() 
    word = resultstring(fullword,'',guessedwords)    
    text.insert(INSERT, HANGED_MAN[6])
    logtext.insert(INSERT,"Welcome, You have 6 tries")
    logtext.pack()
    #Initial data displays
    printtoScreen(word)
    displayHangMan(6)
    displayHangManLog(logmessages[6])


def clicked(alphabet):
    global balancetries    
    global inputword
    global fullword
    global guessedwords    
    inputword = alphabet.upper()
    if(inputword in fullword):
        if(inputword not in guessedwords):
            guessedwords.append(inputword)
    else:
        balancetries -= 1    
    fill()   
    
    if(balancetries ==0):                
        if (messagebox.askyesno("Game Over","You lose !!, Do you want to play again ?") == True):
            startthegame()
        else:
            root.destroy()
        

def fill():  
    printtoScreen(resultstring(fullword,inputword,guessedwords))
    displayHangMan(balancetries) 
    displayHangManLog(logmessages[balancetries])

startthegame()

root.mainloop()

