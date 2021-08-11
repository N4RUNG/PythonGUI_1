from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

buttonNum = Button(root, text="num", width=5, height=2)
buttonDiv = Button(root, text=" / ", width=5, height=2)
buttonMul = Button(root, text=" * " , width=5, height=2)
buttonSub = Button(root, text=" - ", width=5, height=2)
buttonAdd = Button(root, text=" + ", width=5, height=2)
buttonComma = Button(root, text=".", width=5, height=2)
buttonEnter = Button(root, text="┚", width=5, height=2)

button0 = Button(root, text="0", width=5, height=2)
button1 = Button(root, text="1", width=5, height=2)
button2 = Button(root, text="2", width=5, height=2)
button3 = Button(root, text="3", width=5, height=2)
button4 = Button(root, text="4", width=5, height=2)
button5 = Button(root, text="5", width=5, height=2)
button6 = Button(root, text="6", width=5, height=2)
button7 = Button(root, text="7", width=5, height=2)
button8 = Button(root, text="8", width=5, height=2)
button9 = Button(root, text="9", width=5, height=2)

# 첫 째줄
buttonNum.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # row= 는 세로(열)
buttonDiv.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3) # column= 은 가로(행)
buttonMul.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3) # sticky= 는 원하는 방향으로 채울 수 있음. (North + East + West + South) (오왼)
buttonSub.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3) # padx= 와 pady= 는 그리드 사이의 간격 주기

# 둘 째줄
button7.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
button8.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
button9.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
buttonAdd.grid(row=1, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspan= 은 row 를 합칠 개수

# 셋 째줄
button4.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
button5.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
button6.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)

# 넷 째줄
button1.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
button2.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
button3.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
buttonEnter.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# 다섯 쨰줄
button0.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
buttonComma.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()