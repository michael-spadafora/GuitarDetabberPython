from tkinter import filedialog
from tkinter import *



top = Tk()

width = 2000
height = 370
canvas = Canvas(top, width =width, height = height)

def convert():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    f  = open (filename, "r")
    f1 = f.readlines()

button = Button(top, text = "choose file",command = convert)
canvas.pack()
button.pack()

start =  50
interval = 60
i = 0
while i <5:
    canvas.create_line(0,start+i*interval, width, start+i*interval)
    i+=1
# canvas.create_oval(50,50,50,80, fill = "yellow")
# canvas.create_rectangle(50, 20, 150, 80, fill="#476042")


top.mainloop()