from tkinter import * # tkinter

root = Tk()
root.title("GUI") # 타이틀
root.geometry("640x480+100+100") # 가로*세로 // X로 곱하기를 적음 (가로x세로+x좌표+y좌표(어디 뜨게 할지))
root.resizable(False, False) # (x, y) 값 변경 불가 (창 크기 변경 불가)

root.mainloop() # 창이 닫히지 않도록 하는 것