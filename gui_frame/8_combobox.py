from tkinter import *
import tkinter.ttk as ttk # 콤보박스는 .ttk 를 따로 가져와야 함.

root = Tk()
root.title("GUI")
root.geometry("640x480")

combo1 = [f"{str(i)}일" for i in range(1, 32)] # 1부터 31까지 combo1 에 리스트로 담음.
combobox1 = ttk.Combobox(root, height=5, values=combo1) # values= 로 콤보박스에 넣을 값들을 리스트로 가져옴.
combobox1.pack()
combobox1.set("카드 결제일") # 최초 목록 제목

combobox2 = ttk.Combobox(root, height=10, values=combo1, state="readonly") # read only. 즉, 읽기만 가능하고 작성은 불가함.
combobox2.current(0) # 0번째 값을 선택함.
combobox2.pack()

def btcmd():
    print(combobox1.get()) # 여기선 values= 값이 아니라 콤보박스에서 선택한 값을 출력.
    print(combobox2.get())
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()