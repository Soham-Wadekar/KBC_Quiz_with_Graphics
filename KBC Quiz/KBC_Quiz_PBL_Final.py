# Importing libraries

from tkinter import *
from random import *
import numpy as np

# Importing User Defined Modules

from Questions import *
from Instruction import *

# Choosing Random Questions according to difficulty

rand_ques_easy = np.random.permutation(15)[:5]
rand_ques_med = np.random.permutation(15)[:5]
rand_ques_hard = np.random.permutation(10)[:5]

rand_ques = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

ques = []

optA = []
optB = []
optC = []
optD = []

optA_ans = []
optB_ans = []
optC_ans = []
optD_ans = []

audienceOptA = []
audienceOptB = []
audienceOptC = []
audienceOptD = []

for i in rand_ques_easy:
    ques.append(easy_ques[i])
    
    optA.append(optA_easy[i])
    optB.append(optB_easy[i])
    optC.append(optC_easy[i])
    optD.append(optD_easy[i])
    
    optA_ans.append(optA_easy_ans[i])
    optB_ans.append(optB_easy_ans[i])
    optC_ans.append(optC_easy_ans[i])
    optD_ans.append(optD_easy_ans[i])
    
    audienceOptA.append(audienceOptA_easy[i])
    audienceOptB.append(audienceOptB_easy[i])
    audienceOptC.append(audienceOptC_easy[i])
    audienceOptD.append(audienceOptD_easy[i])
    
for i in rand_ques_med:
    ques.append(med_ques[i])
    
    optA.append(optA_med[i])
    optB.append(optB_med[i])
    optC.append(optC_med[i])
    optD.append(optD_med[i])
    
    optA_ans.append(optA_med_ans[i])
    optB_ans.append(optB_med_ans[i])
    optC_ans.append(optC_med_ans[i])
    optD_ans.append(optD_med_ans[i])
    
    audienceOptA.append(audienceOptA_med[i])
    audienceOptB.append(audienceOptB_med[i])
    audienceOptC.append(audienceOptC_med[i])
    audienceOptD.append(audienceOptD_med[i])
    
for i in rand_ques_hard:
    ques.append(hard_ques[i])
    
    optA.append(optA_hard[i])
    optB.append(optB_hard[i])
    optC.append(optC_hard[i])
    optD.append(optD_hard[i])
    
    optA_ans.append(optA_hard_ans[i])
    optB_ans.append(optB_hard_ans[i])
    optC_ans.append(optC_hard_ans[i])
    optD_ans.append(optD_hard_ans[i])
    
    audienceOptA.append(audienceOptA_hard[i])
    audienceOptB.append(audienceOptB_hard[i])
    audienceOptC.append(audienceOptC_hard[i])
    audienceOptD.append(audienceOptD_hard[i])
    
    
ques.append('')

optA.append('')
optB.append('')
optC.append('')
optD.append('')

# For choosing random flip question
ran_choose_flip = randint(0,5)
ran_flip = ran_choose_flip-1

# GUI for Lifelines and Question

root = Tk()
root.geometry("1050x1000")
root.configure(bg='navy')

ques_no = 0

A_P = PhotoImage(file='Audience Poll.png')
Audience_Poll = Button(root,image=A_P,height=100,width=200,pady=50,bg='#A020F0',activebackground='navy')
Audience_Poll.grid(row=0,column=0)

F_F = PhotoImage(file='50-50.png')
Fifty_Fifty = Button(root,image=F_F,height=100,width=200,pady=50,bg='#A020F0',activebackground='navy')
Fifty_Fifty.grid(row=0,column=1)

P = PhotoImage(file='Pass.png')
Pass = Button(root,image=P,height=100,width=200,pady=50,bg='#A020F0',activebackground='navy')
Pass.grid(row=0,column=2)

FTQ = PhotoImage(file='Flip.png')
Flip = Button(root,image=FTQ,height=100,width=200,pady=50,bg='#A020F0',activebackground='navy')
Flip.grid(row=0,column=3)

Amount_Display = Label(root,text="",height=4,width=33,bg="navy",fg='gold',font=("Times New Roman",20),justify=LEFT)
Amount_Display.grid(row=1,columnspan=2)

Lifeline_Display = Label(root,text="\n\n\n",height=4,width=25,bg='navy',fg='gold',font=("Times New Roman",15))
Lifeline_Display.grid(row=1,column=2,columnspan=2)

Question = Label(root,text="",height=3,width=70,pady=25,bg='#A020F0',fg="gold",font=("Times New Roman",20))
Question.config(text="Let's play Kaun Banega Crorepati!!")
Question.grid(row=3,rowspan=2,columnspan=4)

# Click and Lifeline Functions

ques_no = 0
garbage_list = ['X']

def Next():
    global ques_no
    global ran
    
    ran = rand_ques[ques_no]
    
    for i in range(len(garbage_list)):
        if (i==ques_no):
            Question.config(text=ques[ran])
            Option_A.config(text="A. "+optA[ran])
            Option_A.config(relief=RAISED,state=NORMAL,bg='#A020F0',fg='gold')
            Option_B.config(text="B. "+optB[ran])
            Option_B.config(relief=RAISED,state=NORMAL,bg='#A020F0',fg='gold')
            Option_C.config(text="C. "+optC[ran])
            Option_C.config(relief=RAISED,state=NORMAL,bg='#A020F0',fg='gold')
            Option_D.config(text="D. "+optD[ran])
            Option_D.config(relief=RAISED,state=NORMAL,bg='#A020F0',fg='gold') 
            
            Amount_Display.config(text="You won Rs."+str(amount_won[ques_no-1])+"!!")
            
            Option_A.config(command=ClickA)
            Option_B.config(command=ClickB)
            Option_C.config(command=ClickC)
            Option_D.config(command=ClickD)
            
            Audience_Poll.config(command=Audience)
            Fifty_Fifty.config(command=FiftyFifty)
            Pass.config(command=PASS)
            Flip.config(command=flip)
            
            quit.config(command=Quit)
            
            Lifeline_Display.config(text="")
            
            ques_no = ques_no + 1
            garbage_list.append('X')
        else:
            continue
            
            
        if ques_no==16:
            next_ques.config(state=DISABLED,text="")
            Question.config(bg="green",text="You won 1 crore!!!")
            Option_A.config(state=DISABLED,text="")
            Option_B.config(state=DISABLED,text="")
            Option_C.config(state=DISABLED,text="")
            Option_D.config(state=DISABLED,text="")
            Amount_Display.config(text="")
            Audience_Poll.config(state=DISABLED)
            Fifty_Fifty.config(state=DISABLED)
            Pass.config(state=DISABLED)
            Flip.config(state=DISABLED)
            quit.config(text="",state=DISABLED)
            Instructions.config(text="",state=DISABLED)
        if ques_no==0:
            next_ques.config(text="Start")
        elif ques_no==1:
            Amount_Display.config(text="")
            next_ques.config(text="Next Question")
        elif ques_no==15:
            next_ques.config(text="Finish")
        elif ques_no==16:
            next_ques.config(text="")
        else:
            next_ques.config(text="Next Question")
            
        next_ques.config(state=DISABLED)
        
# Option Click Buttons
            
def ClickA():
            Option_A.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_B.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optA[ran]==optA_ans[ran]:
                Option_A.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_A.config(bg='red',fg='gold')
                exit()
                
def ClickB():
            Option_B.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optB[ran]==optB_ans[ran]:
                Option_B.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_B.config(bg='red',fg='gold')
                exit()
                
def ClickC():
            Option_C.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_B.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optC[ran]==optC_ans[ran]:
                Option_C.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_C.config(bg='red',fg='gold')
                exit()

def ClickD():
            Option_D.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_B.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optD[ran]==optD_ans[ran]:
                Option_D.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_D.config(bg='red',fg='gold')
                exit()
                
# Flip Option Click Buttons

def ClickA_flip():
            Option_A.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_B.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optA_flip[ran_flip]==optA_flip_ans[ran_flip]:
                Option_A.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_A.config(bg='red',fg='gold')
                exit()
                
def ClickB_flip():
            Option_B.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optB_flip[ran_flip]==optB_flip_ans[ran_flip]:
                Option_B.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_B.config(bg='red',fg='gold')
                exit()
                
def ClickC_flip():
            Option_C.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_B.config(state=DISABLED)
            Option_D.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optC_flip[ran_flip]==optC_flip_ans[ran_flip]:
                Option_C.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_C.config(bg='red',fg='gold')
                exit()

def ClickD_flip():
            Option_D.config(relief=SUNKEN,bg='gold',fg='#A020F0')
            Option_A.config(state=DISABLED)
            Option_B.config(state=DISABLED)
            Option_C.config(state=DISABLED)
            for time in range(50000000):
                pass
            if optD_flip[ran_flip]==optD_flip_ans[ran_flip]:
                Option_D.config(bg='green',fg='gold')
                enable_next_ques()
            else:
                Option_D.config(bg='red',fg='gold')
                exit()
                
# Audience Poll

def Audience():
    Audience_Answers = 'A)'+str(audienceOptA[ran])+'%\n'+'B)'+str(audienceOptB[ran])+'%\n'+'C)'+str(audienceOptC[ran])+'%\n'+'D)'+str(audienceOptD[ran])+'%'
    Lifeline_Display.config(text=Audience_Answers)
    Audience_Poll.config(state=DISABLED)
    
def Audience_flip():
    Audience_Answers_flip = 'A)'+str(audienceOptA_flip[ran_flip])+'%\n'+'B)'+str(audienceOptB_flip[ran_flip])+'%\n'+'C)'+str(audienceOptC_flip[ran_flip])+'%\n'+'D)'+str(audienceOptD_flip[ran_flip])+'%'
    Lifeline_Display.config(text=Audience_Answers_flip)
    Audience_Poll.config(state=DISABLED)
    
# Fifty Fifty
    
def FiftyFifty():
    global randomness
    randomness = randint(0,2)
    
    if optA_ans[ran]!=' ':
        if randomness==0:
            Option_C.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_B.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_B.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
            
    elif optB_ans[ran]!=' ':
        if randomness==0:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
    
    elif optC_ans[ran]!=' ':
        if randomness==0:
            Option_B.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_B.config(state=DISABLED,text=" ")
            
    elif optD_ans[ran]!=' ':
        if randomness==0:
            Option_B.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_B.config(state=DISABLED,text=" ")
    
    Fifty_Fifty.config(state=DISABLED)
    
def FiftyFifty_flip():
    global randomness
    randomness = randint(0,2)
    
    if optA_flip_ans[ran_flip]!=' ':
        if randomness==0:
            Option_C.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_B.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_B.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
            
    elif optB_flip_ans[ran_flip]!=' ':
        if randomness==0:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
    
    elif optC_flip_ans[ran_flip]!=' ':
        if randomness==0:
            Option_B.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_D.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_B.config(state=DISABLED,text=" ")
            
    elif optD_flip_ans[ran_flip]!=' ':
        if randomness==0:
            Option_B.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==1:
            Option_A.config(state=DISABLED,text=" ")
            Option_C.config(state=DISABLED,text=" ")
        elif randomness==2:
            Option_A.config(state=DISABLED,text=" ")
            Option_B.config(state=DISABLED,text=" ")
    
    Fifty_Fifty.config(state=DISABLED)
        
# Pass
    
def PASS():
    Pass_Answer = str(optA_ans[ran])+'\n'+str(optB_ans[ran])+'\n'+str(optC_ans[ran])+'\n'+str(optD_ans[ran])
    Lifeline_Display.config(text=Pass_Answer)
    Pass.config(state=DISABLED)
    
def PASS_flip():
    Pass_Answer = str(optA_flip_ans[ran_flip])+'\n'+str(optB_flip_ans[ran_flip])+'\n'+str(optC_flip_ans[ran_flip])+'\n'+str(optD_flip_ans[ran_flip])
    Lifeline_Display.config(text=Pass_Answer)
    Pass.config(state=DISABLED)
    
# Flip
    
def flip():
    Question.config(text=flip_ques[ran_flip])
    Option_A.config(text="A. "+optA_flip[ran_flip],state=NORMAL)
    Option_B.config(text="B. "+optB_flip[ran_flip],state=NORMAL)
    Option_C.config(text="C. "+optC_flip[ran_flip],state=NORMAL)
    Option_D.config(text="D. "+optD_flip[ran_flip],state=NORMAL)
    
    Option_A.config(command=ClickA_flip)
    Option_B.config(command=ClickB_flip)
    Option_C.config(command=ClickC_flip)
    Option_D.config(command=ClickD_flip)
    
    Audience_Poll.config(command=Audience_flip)
    Fifty_Fifty.config(command=FiftyFifty_flip)
    Pass.config(command=PASS_flip)
    
    Flip.config(state=DISABLED)
    
# Quit Button
    
def Quit():
    next_ques.config(state=DISABLED,text="")
    Question.config(bg="green",text="You won Rs."+str(amount_won[ques_no-2]))
    Option_A.config(state=DISABLED,text="")
    Option_B.config(state=DISABLED,text="")
    Option_C.config(state=DISABLED,text="")
    Option_D.config(state=DISABLED,text="")
    Amount_Display.config(text="")
    Audience_Poll.config(state=DISABLED)
    Fifty_Fifty.config(state=DISABLED)
    Pass.config(state=DISABLED)
    Flip.config(state=DISABLED)
    quit.config(text="",state=DISABLED)  
    Instructions.config(text="",state=DISABLED)
    
# Wrong Answer Mechanism
    
def exit():
    next_ques.config(state=DISABLED,text="")
    if amount_won[ques_no-2]>=amount_won[4] and amount_won[ques_no-2]<amount_won[9]:
        Question.config(bg="red",text="Your answer is wrong.You dropped to Rs."+str(amount_won[4]))
    elif amount_won[ques_no-2]>=amount_won[9]:
        Question.config(bg="red",text="Your answer is wrong.You dropped to Rs."+str(amount_won[9]))
    else:
        Question.config(bg="red",text="Your answer is wrong.You won Rs.0")
    Option_A.config(state=DISABLED,text="",bg="#A020F0")
    Option_B.config(state=DISABLED,text="",bg="#A020F0")
    Option_C.config(state=DISABLED,text="",bg="#A020F0")
    Option_D.config(state=DISABLED,text="",bg="#A020F0")
    Amount_Display.config(text="")
    Audience_Poll.config(state=DISABLED)
    Fifty_Fifty.config(state=DISABLED)
    Pass.config(state=DISABLED)
    Flip.config(state=DISABLED)
    quit.config(text="",state=DISABLED)
    Instructions.config(text="",state=DISABLED)
    
def enable_next_ques():
    next_ques.config(state=NORMAL)
    
# Instructions Button

def instructions():
    top = Tk()
    
    Label(top,text=Inst,bg='navy',fg='gold',font=("Times New Roman",16)).pack()
    
    top.mainloop()

# GUI for Option Buttons

Option_A = Button(root,text="",height=1,width=40,pady=25,bg='#A020F0',fg='gold',font=("Times New Roman",16),activebackground='gold',activeforeground='#A020F0')
Option_A.grid(row=5,column=0,columnspan=2)

Option_B = Button(root,text="",height=1,width=40,pady=25,bg='#A020F0',fg='gold',font=("Times New Roman",16),activebackground='gold',activeforeground='#A020F0')
Option_B.grid(row=5,column=2,columnspan=2)

Option_C = Button(root,text="",height=1,width=40,pady=25,bg='#A020F0',fg='gold',font=("Times New Roman",16),activebackground='gold',activeforeground='#A020F0')
Option_C.grid(row=6,column=0,columnspan=2)

Option_D = Button(root,text="",height=1,width=40,pady=25,bg='#A020F0',fg='gold',font=("Times New Roman",16),activebackground='gold',activeforeground='#A020F0')
Option_D.grid(row=6,column=2,columnspan=2)

Instructions = Button(root,text="Instructions",height=3,width=10,bg='#A020F0',fg='gold',activebackground='gold',activeforeground='#A020F0',font=("Times New Roman",16),command=instructions)
Instructions.grid(row=7,column=0)

next_ques = Button(root,text="Start",width=50,height=1,pady=25,bg='#A020F0',fg='gold',font=("Times New Roman",16),command=Next,activebackground='gold',activeforeground='#A020F0')
next_ques.grid(row=7,column=1,columnspan=2)

quit = Button(root,text="Quit",height=3,width=10,bg='#A020F0',fg='gold',activebackground='gold',activeforeground='#A020F0',font=("Times New Roman",16))
quit.grid(row=7,column=3)

root.mainloop()