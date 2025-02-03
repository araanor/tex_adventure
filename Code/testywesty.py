import tkinter as tk
import time



def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char)
        Label.update()
        time.sleep(.25)

root = tk.Tk()
text = "Hello world!"
Label = tk.Label(root)
Label.pack()
printString(text)
root.mainloop()