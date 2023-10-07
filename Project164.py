from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Rotator')
root.geometry('600x600')
root.configure(background = 'snow')

lblImg = Label(root, highlightthickness = 5)
lblImg.place(relx = 0.5, rely = 0.5, anchor = CENTER)

entPath = Entry(root)
entPath.place(relx = 0.5, rely = 0.2, anchor = CENTER)

def openImg(path):
    img = ImageTk.PhotoImage(Image.open('Project164+/' + path + '.png'))
    lblImg['image'] = img

btnOpen = Button(root, text = 'Open Image', command = lambda: openImg(entPath.get()))
btnOpen.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()