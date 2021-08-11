from tkinter import *
import tkinter.messagebox as  msgbox # 메시지박스

root = Tk()
root.title("GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "알림입니다.") # 알림창 (i)
Button(root, text="알림", command=info).pack()

def warning():
    msgbox.showwarning("경고", "경고입니다.") # 경고창 (!)
Button(root, text="경고", command=warning).pack()

def error():
    msgbox.showerror("에러", "에러입니다.") # 경고창 (×)
Button(root, text="에러", command=error).pack()

def okcancel():
    msgbox.askokcancel("확인 취소", "확인 하시겠습니까?") # 확인, 취소 (?)
Button(root, text="확인 취소", command=okcancel).pack()

def retrycancel():
    response = msgbox.askretrycancel("재시도 취소", "다시 시도 하시겠습니까?") # 다시 시도 (!)
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")
Button(root, text="재시도", command=retrycancel).pack()

def yesno():
    msgbox.askyesno("예 아니오", "선택 하시겠습니까?") # 예, 아니오 (?)
Button(root, text="예 아니오", command=yesno).pack()

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="바로 종료하시겠습니까?") # 예, 아니오, 취소 (?)
    if response == 1: # 예: True -> 1 // 아니오: False -> 0 // 취소: None 0 -> 그 외
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")
Button(root, text="예 아니오 취소", command=yesnocancel).pack()

root.mainloop()