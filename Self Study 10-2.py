from tkinter import *
import random  


window = Tk()
window.geometry("210x210")


canvas = Canvas(window, width=200, height=200)
canvas.pack()


fNameList = ["image1.gif", "image2.gif", "image3.gif", "image4.gif",
             "image5.gif", "image6.gif", "image7.gif", "image8.gif", "image9.gif"]

random.shuffle(fNameList)


photoList = [None] * 9


def create_image_on_canvas(image_path, x, y):
    img = PhotoImage(file=image_path)
    canvas.create_image(x, y, image=img, anchor=NW)
    return img


image_path = "C:/Users/admin/Desktop/image/"


xPos, yPos = 5, 5  
for i in range(3):
    for j in range(3):
        img_path = image_path + fNameList[i*3+j] 
        photoList[i*3+j] = create_image_on_canvas(img_path, xPos, yPos)
        xPos += 70  
    xPos = 5  
    yPos += 70  

window.mainloop()
