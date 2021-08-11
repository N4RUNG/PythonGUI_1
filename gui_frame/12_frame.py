from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해주세요.").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

frame1 = Frame(root, relief="solid", bd=1) # relief= 는 테두리 모양, bd= 는 외곽선
frame1.pack(side="left", fill="both", expand=True) # side= 는 상하좌우 위치, fill= 은 채우기, expand= 는 가운데까지 확장
Button(frame1, text="불고기버거").pack()
Button(frame1, text="띠드버거").pack()
Button(frame1, text="치킨버거").pack()

frame2 = LabelFrame(root, text="음료") # 텍스트가 있는 프레임
frame2.pack(side="right", fill="both", expand=True)
Button(frame2, text="제로콜라").pack()
Button(frame2, text="마운틴듀").pack()

root.mainloop()