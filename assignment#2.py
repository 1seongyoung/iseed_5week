#문제 5번

from tkinter import *
from time import sleep


fNameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", 
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

num = 0


def clickNext():
    global num
    num += 1  
    if num == len(fNameList):  
        num = 0  
    pLabel.config(text=fNameList[num]) 


def clickPrev():
    global num
    num -= 1 
    if num < 0: 
        num = len(fNameList) - 1  
    pLabel.config(text=fNameList[num])  


window = Tk()
window.geometry("300x100") 


buttonPrev = Button(window, text="<< 이전", command=clickPrev)
buttonPrev.pack(side=LEFT, padx=20)  


pLabel = Label(window, text=fNameList[num])
pLabel.pack(side=LEFT)


buttonNext = Button(window, text="다음 >>", command=clickNext)
buttonNext.pack(side=LEFT, padx=20)  


window.mainloop()