from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI Project")

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 파일 프레임 >> 파일 추가 버튼 >> 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", # 타이틀
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*"))) # 파일 타입
    for file in files:
        file_list.insert(END, file) # 파일 리스트에 파일경로 추가

# 파일 프레임 >> 파일 추가 버튼
add_file_btn = Button(file_frame, text="파일 추가", padx=5, pady=5, width=12, command=add_file)
add_file_btn.pack(side="left")

# 파일 프레임 >> 파일 삭제 버튼 >> 파일 삭제 함수
def del_file():
    for idx in reversed(file_list.curselection()):
        file_list.delete(idx)

# 파일 프레임 >> 파일 삭제 버튼
del_file_btn = Button(file_frame, text="파일 삭제", padx=5, pady=5, width=12, command=del_file)
del_file_btn.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

# 리스트 프레임 >> 스크롤바
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# 리스트 프레임 >> 파일 리스트 (스크롤바)
file_list = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
file_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=file_list.yview)


# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

# 저장 경로 프레임 >> 텍스트
dest_path_txt = Entry(path_frame)
dest_path_txt.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=2) # ipady= 는 in pady로 안의 영역이 넓어지게 함.

# 저장 경로 프레임 >> 찾아보기 버튼 >> 경로 찾기 함수
def dest_path():
    selected_folder = filedialog.askdirectory()
    if selected_folder == None: # 사용자가 취소를 누를 때
        return
    dest_path_txt.delete(0, END)
    dest_path_txt.insert(0, selected_folder)

# 저장 경로 프레임 >> 찾아보기 버튼
dest_path_btn = Button(path_frame, text="찾아보기", width=10, command=dest_path)
dest_path_btn.pack(side="right", padx=5, pady=5)


# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

# 옵션 프레임 >> 1. 가로 넓이 >> 가로 넓이 레이블
width_lbl = Label(option_frame, text="가로 넓이", width=8)
width_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 1. 가로 넓이 >> 가로 넓이 콤보
width_list = ["원본 유지", "1024", "800", "640"]
width_cmb = ttk.Combobox(option_frame, state="readonly", values=width_list, width=8)
width_cmb.current(0) # 기본값
width_cmb.pack(side="left")

# 옵션 프레임 >> 2. 간격 옵션 >> 간격 옵션 레이블
space_lbl = Label(option_frame, text="간격", width=8)
space_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 2. 간격 옵션 >> 간격 옵션 콤보
space_list = ["없음", "좁게", "보통", "넓게"]
space_cmb = ttk.Combobox(option_frame, state="readonly", values=space_list, width=8)
space_cmb.current(0) # 기본값
space_cmb.pack(side="left")

# 옵션 프레임 >> 3. 포맷 >> 포맷 레이블
format_lbl = Label(option_frame, text="포맷", width=8)
format_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 3. 포맷 >> 포맷 콤보
format_list = ["PNG", "JPG", "BMP"]
format_cmb = ttk.Combobox(option_frame, state="readonly", values=format_list, width=8)
format_cmb.current(0) # 기본값
format_cmb.pack(side="left")


# 진행 상황 프레임
progress_frame = LabelFrame(root, text="진행 상황")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

# 진행 상황 프레임 >> 프로그레스바
p_var = DoubleVar() # p_var 실수 선언
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

# 실행 프레임 >> 닫기 버튼
close_btn = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
close_btn.pack(side="right", padx=5, pady=5)

# 실행 프레임 >> 시작 버튼 >> 시작 함수
def start():
    if file_list.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    if len(dest_path_txt.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

# 실행 프레임 >> 시작 버튼
start_btn = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
start_btn.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()