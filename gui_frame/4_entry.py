from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

text1 = Text(root, width=30, height=5) # 텍스트 위젯
text1.pack()
text1.insert(END, "텍스트1") # 값이 비어있으므로 END를 써도 가장 뒤 위치로 이동하지 않는다.

entry1 = Entry(root, width=30) # 한줄 텍스트 위젯 (엔터 없음)
entry1.pack()
entry1.insert(0, "엔트리1") # 적혀 있는 게 없으므로 0 을 적어도 END랑 똑같은 효과를 보여줌.

def btcmd():
    print(text1.get("1.0", END)) # 1은 첫번째 라인부터, 0은 0번째 위치부터, END는 끝까지 가져오란 것
    print(entry1.get())

    text1.delete("1.0", END)
    entry1.delete(0, END) # 줄이 없으므로 0번째 위치부터 끝까지
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()