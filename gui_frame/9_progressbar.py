from tkinter import *
import tkinter.ttk as ttk # 프로그레스바는 .ttk 를 따로 가져와야 함.
import time # 로딩의 느낌을 추가하기 위해 time 을 가져옴.

root = Tk()
root.title("GUI")
root.geometry("640x480")

progressbar1 = ttk.Progressbar(root, maximum=100, mode="determinate")
# maximum= 은 최대값
# mode= 에서 "indeterminate" 는 결정되지 않았다는 뜻으로 진행바가 계속 반복됨.
# mode= 에서 "determinate" 는 진행바가 차오르게 함.
progressbar1.start(10) # start() 으로 시작할 수 있음. ()안에 넣은 10ms 속도로 움직임.
progressbar1.pack()

progress2 = DoubleVar() # 소수점 단위로 올라갈 수 있기 때문에 실수로 정의
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=progress2)
# length= 는 진행바의 길이
# variable= 로 값을 저장할 수 있음.
progressbar2.pack()

def btcmd():
    progressbar1.stop() # 작동 중지

    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        progress2.set(i) # progressbar2 의 값 설정
        progressbar2.update() # 값 업데이트

        print(progress2.get()) # 진행의 정도를 출력
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()