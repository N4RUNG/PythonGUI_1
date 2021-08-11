# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시오.

# [GUI 조건]
# 1. title : 제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램의 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

from tkinter import *
import os

memo = Tk()
memo.title("제목 없음 - Windows 메모장")


# 메뉴
menu = Menu(memo)

file_name = "mynote.txt"

menu_file = Menu(menu, tearoff=0)

# 열기
def open_file(): # 열기 에서 실행할 함수
    if os.path.isfile(file_name): # 경로에 file_name 의 파일이 있는지 확인한다.
        with open(file_name, "r", encoding="utf8") as file: # file_name 을 read 모드로 켜서 file 변수로 저장한다.
            text.delete("1.0", END) # text 의 첫 번째줄 0번째 글자부터 끝까지 지운다.
            text.insert(END, file.read()) # text 의 끝부분에 file 의 내용을 읽어 가져온다. ( 덮어쓰기 )
    else:
        pass
menu_file.add_command(label="열기", command=open_file) # 레이블은 열기, 누르면 open_file 을 실행

# 저장
def save_file(): # 저장 에서 실행할 함수
    with open(file_name, "w", encoding="utf8") as file: # file_name 을 write 모드로 켜서 file 변수로 저장한다.
        file.write(text.get("1.0", END)) # 첫 번째줄 0번째 글자부터 끝까지 가져와서 file 에 쓴다.
menu_file.add_command(label="저장", command=save_file) # 레이블은 저장, 누르면 save_file 을 실행

menu_file.add_separator() # 구분선

# 끝내기
menu_file.add_command(label="끝내기", command=memo.quit) # 레이블은 끝내기, memo.quit 을 실행

# 
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_file)
menu.add_cascade(label="서식", menu=menu_file)
menu.add_cascade(label="보기", menu=menu_file)
menu.add_cascade(label="도움말", menu=menu_file)

memo.config(menu=menu)


# 스크롤바
scrollbar = Scrollbar(memo)
scrollbar.pack(side="right", fill="y")


# 텍스트
text = Text(memo, yscrollcommand=scrollbar.set)
text.pack(fill="both", expand=True)

scrollbar.config(command=text.yview)


memo.mainloop()