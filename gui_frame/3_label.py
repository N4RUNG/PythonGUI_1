from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

label1 = Label(root, text="레이블1")
label1.pack()

photo = PhotoImage(file="gui_frame/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change1():
    label1.config(text="(수정됨)") # .config() 로 원래 있던 속성을 바꿀 수 있음.

    global photo2 # 전역변수로 만들지 않으면 쓸모없는 메모리로 처리해서 지울 수 있음. (적용되자마자 사라지면 갱신이 안되니 이미지가 안뜸)
    photo2 = PhotoImage(file="gui_frame/img2.png")
    label2.config(image=photo2)
button1 = Button(root, text="버튼1", command=change1)
button1.pack()

root.mainloop()