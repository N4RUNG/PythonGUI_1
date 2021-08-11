from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

check1 = IntVar() # check1 을 정수형으로 선언함.
checkbutton1 = Checkbutton(root, text="체크박스1", variable=check1) # variable= 로 check에 체크 값 저장
checkbutton1.select() # 체크 처리
checkbutton1.deselect() # 체크 해제 처리
checkbutton1.pack()

check2 = IntVar()
checkbutton2 = Checkbutton(root, text="체크박스2", variable=check2)
checkbutton2.pack()

def btcmd():
    print(check1.get()) # 0 일 경우 체크 안됨, 1 일 경우 체크 됨.
    print(check2)
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()