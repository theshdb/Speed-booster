import shutil
import os
from tkinter import *

root = Tk()
root.title("PC Speed Booster")
paths = ["C:\\Windows\\prefetch", "C:\\Windows\\Temp", "C:\\Users\\Shada\\AppData\\Local\\Temp"]

def action():
    for path in paths:
        dirContent = os.listdir(path)
        for file in dirContent:
            if os.path.isfile(path + "\\" +file):
                try:
                    os.remove(path + "\\" + file)
                except:
                    pass
            elif os.path.isdir(path + "\\" +file):
                try:
                    shutil.rmtree(path + "\\" +file)
                except:
                    pass


canvas = Canvas(root, height=200, width=400, bg="#0D1F2D")
canvas.pack(fill = BOTH, expand = True)

frame = Frame(root, bg="white")
frame.place(relheight=0.9, relwidth=0.9, relx=0.1, rely=0.2)
labelTitle = Label(frame, text="Speed up your computer with a click", font = ('Helvetica', 15, 'bold'), height= 2,
                bg="ghostWhite", fg="#74A059")
labelTitle.pack()
labelTitle.place(x=5, y=0, rely=0.1)

btnboost = Button(frame, text="Boost", font = ('Helvetica', 9, 'bold'), padx=10, pady=5, fg="white", bg="#0D1F2D", 
                command=action, activeforeground = "red")
btnboost.pack()
btnboost.place(x=180, y=140, anchor=CENTER)

inputtxt = Text(frame, height = 1.8,
                width = 20, bg = "light grey")
inputtxt.pack()
inputtxt.place(x=150, y=69)

labelName = Label(frame, text="PC Name", font = ('Helvetica', 12, 'bold'), height= 2,
                    bg="ghostWhite", fg="#435868")
labelName.pack()
labelName.place(x=50, y=69)
root.mainloop()