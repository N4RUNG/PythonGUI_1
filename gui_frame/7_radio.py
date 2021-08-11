from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

label1 = Label(root, text="버거를 선택하세요.").pack() # .pack() 을 뒤에 붙이면 바로 띄울 수 있으나, 값 수정이 안됨.

radio1 = IntVar() # Int형 선언
radiobutton1 = Radiobutton(root, text="불고기버거", value=1, variable=radio1)
radiobutton2 = Radiobutton(root, text="치즈버거", value=2, variable=radio1)
radiobutton3 = Radiobutton(root, text="치킨버거", value=3, variable=radio1)
radiobutton1.select()

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

label2 = Label(root, text="\n음료를 선택하세요.").pack()

radio2 = StringVar() # String형. 즉, 자료형 선언.
radiobutton4 = Radiobutton(root, text="제로콜라", value="콜라", variable=radio2)
radiobutton5 = Radiobutton(root, text="마운틴듀", value="마운틴듀", variable=radio2)
radiobutton4.select()

radiobutton4.pack()
radiobutton5.pack()

def btcmd():
    print(f"버거 : {radio1.get()}") # 위에서 설정한 value= 값을 가져옴.
    print(f"음료 : {radio2.get()}")
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()