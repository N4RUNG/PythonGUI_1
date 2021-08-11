from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

frame1 = Frame(root)
frame1.pack()

scrollbar1 = Scrollbar(frame1)
scrollbar1.pack(side="right", fill="y")

listbox1 = Listbox(frame1, selectmode="extended", height=10, yscrollcommand=scrollbar1.set)

for i in range(1, 32):
    listbox1.insert(END, f"{str(i)} 일")
listbox1.pack(side="left")

scrollbar1.config(command=listbox1.yview)

root.mainloop()