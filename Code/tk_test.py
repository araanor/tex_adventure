import tkinter as tk
import time


window = tk.Tk()
window.title("testy")
#window.attributes("-fullscreen", True)

CRV = 11


button_labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

for i in range(0, CRV):
    window.columnconfigure(i, weight=1, minsize=1)
    window.rowconfigure(i, weight=1, minsize=1)


content = tk.Frame(window)       
txt_frm = tk.Frame(content, borderwidth=5, relief="raised", width=1680, height=100)
txt = tk.Label(txt_frm, text="", wraplength=1680)
btn_frm = tk.Frame(content, borderwidth=5, relief="raised", width=1680, height=100)
#inv_btn = tk.Button(btn_frm, text="Inventory")
#skill_btn = tk.Button(btn_frm, text="Skills")
#atk_btn = tk.Button(btn_frm, text="Attack")
x= -1
for i in range(0,5):
    btn_frm.columnconfigure(i, weight=1, minsize=1)
    btn_frm.rowconfigure(i, weight=1, minsize=1)
    
    for j in range(0, 5):
        button = tk.Button(
            master=btn_frm,
            relief=tk.RAISED,
            borderwidth=1
        )
        x+=1
        button.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=button, text=button_labels[x])
        label.pack(padx=5, pady=5)


def printString(string):
    for char in string:
        txt.configure(text=txt.cget('text') + char)
        txt.update()
        time.sleep(.25)

content.grid(column=0, row=0)
txt_frm.grid(column=0, row=0, columnspan=10,rowspan=5, sticky="nsew")
txt.pack(fill="both")
btn_frm.grid(column=0,row=5,columnspan=10,rowspan=5,sticky="nsew")
#inv_btn.grid(column=0,row=0,columnspan=2,rowspan=2)
#skill_btn.grid(column=3,row=0,columnspan=2,rowspan=2)
#atk_btn.grid(column=5,row=0,columnspan=2,rowspan=2)

text = "this is the main text box for the word adventure game that i am making right now."
printString(text)

window.mainloop()