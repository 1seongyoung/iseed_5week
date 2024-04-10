
#문제 3번
from tkinter import *

window = Tk()

def rdo_change():
    if var.get() == 1:
        label1.configure(text="파리")
    else:
        label1.configure(text="프랑스")

var = IntVar()  # IntVar 객체 생성
rdo1 = Radiobutton(window, text="파리", variable=var, value=1, command=rdo_change)
rdo2 = Radiobutton(window, text="프랑스", variable=var, value=2, command=rdo_change)
label1 = Label(window, text="선택한 값을 표시", fg="red")

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()




#;#######################

#문제 4번
from tkinter import *

window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

#4-1
button1.pack(side=TOP)  # 세로 정렬을 위해 TOP 사용
button2.pack(side=TOP)
button3.pack(side=TOP)

#4-2
#button3.pack(side=BOTTOM)
#button2.pack(side=BOTTOM)
#button1.pack(side=BOTTOM)

#4-3
#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)

#4-4
#button3.pack(side=RIGHT)
#button2.pack(side=RIGHT)
#button1.pack(side=RIGHT)

window.mainloop()