from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

button1 = Button(root, text="버튼1") # 버튼 생성
button1.pack() # .pack() 을 해야만 maimloop 에 포함됨

button2 = Button(root, padx=10, pady=10, text="버튼2") # padx= 는 가로 여백, pady= 는 세로 여백 ( 늘릴 여백 크기 )
button2.pack()

button3 = Button(root, width=10, height=5, text="버튼3") # width= 는 가로 길이, height= 는 세로 길이 ( 고정 크기 )
button3.pack()

button4 = Button(root, fg="white", bg="black", text="버튼4") # fg= 는 글자색, bg= 는 배경색
button4.pack()

photo = PhotoImage(file="gui_frame/img.png")
button5 = Button(root, image=photo) # image= 로 버튼을 이미지로 설정 가능
button5.pack()

def btcmd():
    print("클릭")
button6 = Button(root, text="버튼6", command=btcmd) # command= 로 함수 실행 가능
button6.pack()

root.mainloop()