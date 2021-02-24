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


canvas = Canvas(root, height=200, width=400, bg="#263D42")
canvas.pack(fill = BOTH, expand = True)

frame = Frame(root, bg="white")
frame.place(relheight=0.9, relwidth=0.9, relx=0.1, rely=0.2)
label = Label(frame, text="Speed up your computer with a click", font = ('Helvetica', 15, 'bold'), height= 2, bg="ghostWhite", fg="red")
label.pack()
label.place(relx = 0.0, rely=0.1)

boost = Button(frame, text="Boost", font = ('Helvetica', 9, 'bold'), padx=10, pady=5, fg="white", bg="#263D42", command=action, activeforeground = "red")
boost.pack()
boost.place(relx=0.5, rely= 0.55, anchor=CENTER)

root.mainloop()