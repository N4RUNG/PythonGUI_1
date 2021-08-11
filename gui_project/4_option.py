from tkinter import * # 전체적인 UI 구축
import tkinter.ttk as ttk # 콤보박스, 프로그레스바 ( __all__ 에 포함되지 않는 것들 )
from tkinter import filedialog # 가져올 파일, 선택할 폴더 설정하게 하기
import tkinter.messagebox as msgbox # 메시지 박스 띄우기 ( 경고, 에러, 완료 메시지 박스 )
from PIL import Image # 이미지 열기, 이미지 만들기
import os # 경로 작업 ( 경로 확인, 특정 경로에 파일 저장 )
import time # 파일 이름 시간으로 저장

root = Tk()
root.title("GUI Project")

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 파일 프레임 >> 파일 추가 버튼 >> 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", # 타이틀
        filetypes=(("PNG 파일, JPG 파일", "*.png, *.jpg"), ("모든 파일", "*.*")), # 파일 타입
        initialdir=os.getcwd())
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
    if selected_folder == "": # 사용자가 취소를 누를 때 // None 으로 하면 안 되고 빈 문자열로 해야 함.
        return
    dest_path_txt.delete(0, END)
    dest_path_txt.insert(0, selected_folder)

# 저장 경로 프레임 >> 찾아보기 버튼
dest_path_btn = Button(path_frame, text="찾아보기", width=10, command=dest_path)
dest_path_btn.pack(side="right", padx=5, pady=5)


# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

# 옵션 프레임 >> 1. 가로 길이 >> 가로 길이 레이블
width_lbl = Label(option_frame, text="가로 길이", width=10)
width_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 1. 가로 넓이 >> 가로 넓이 콤보
width_list = ["원본 유지", "1024", "800", "640"]
width_cmb = ttk.Combobox(option_frame, state="readonly", values=width_list, width=10)
width_cmb.current(0) # 기본값
width_cmb.pack(side="left")

# 옵션 프레임 >> 2. 간격 옵션 >> 간격 옵션 레이블
space_lbl = Label(option_frame, text="간격", width=8)
space_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 2. 간격 옵션 >> 간격 옵션 콤보
space_list = ["없음", "좁게", "보통", "넓게"]
space_cmb = ttk.Combobox(option_frame, state="readonly", values=space_list, width=10)
space_cmb.current(0) # 기본값
space_cmb.pack(side="left")

# 옵션 프레임 >> 3. 포맷 >> 포맷 레이블
format_lbl = Label(option_frame, text="포맷", width=8)
format_lbl.pack(side="left", padx=5, pady=5)

# 옵션 프레임 >> 3. 포맷 >> 포맷 콤보
format_list = ["PNG", "JPG", "BMP"]
format_cmb = ttk.Combobox(option_frame, state="readonly", values=format_list, width=10)
format_cmb.current(0) # 기본값
format_cmb.pack(side="left", padx=5, pady=5)


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
    try:
        # 이미지 파일 확인
        if file_list.size() == 0:
            msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
            return
        
        # 저장 경로 확인
        if len(dest_path_txt.get()) == 0:
            msgbox.showwarning("경고", "저장 경로를 선택하세요.")
            return
        
        # 실행 프레임 >> 시작 버튼 >> 시작 함수 >> 이미지 통합
        # 가로 길이
        img_width = width_cmb.get()
        if img_width == "원본 유지":
            img_width = -1 # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)
        
        # 간격
        img_space = space_cmb.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else: # 없음
            img_space = 0

        # 포맷
        img_format = format_cmb.get().lower() # PNG JPG BMP 파일을 가져와서 소문자로 변경

        # 이미지 크기 가져오기
        images = [Image.open(x) for x in file_list.get(0, END)]
        image_sizes = [] # [(width1, height1), (width2, height2), ...]

        if img_width > -1: # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images] # x:y = a:b 일 때 bx = ay 이므로 b = ax/y
        else: # 원본 width 값 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*image_sizes) # x.size 가 ((10, 10), (20, 20), (30, 30)) 같이 묶여있었던 것을 (10, 10) (20, 20) (30, 30) 이런식으로 리스트를 풀음.

        # 최대 가로 길이, 전체 세로 길이
        max_width, total_height = max(widths), sum(heights)

        # 배경
        if img_space > 0: # 간격이 있다면
            total_height += (img_space * (len(images) - 1)) # 전체 세로 길이 추가

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0 # y 위치

        for idx, img in enumerate(images):
            # width가 원본유지가 아니라면 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            # 이미지 합치기
            result_img.paste(img, (0,  y_offset)) # x는 0, y는 y_offset 의 위치에 img사진을 붙여넣음.
            y_offset += (img.size[1] + img_space)# height와 간격만큼 더해줌
            
            # 프로그레스 업데이트
            progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보 계산 ( idx 는 0부터 시작하므로 1을 더해줌 )
            p_var.set(progress) # 프로그레스바 설정
            progress_bar.update() # 프로그레스바 업데이트
        
        # 파일 이름과 포맷 설정
        file_name = time.strftime(f"%Y%m%d%H%M%S.{img_format}")

        # 파일 저장
        dest_path = os.path.join(dest_path_txt.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    
    except Exception as err: # 뭔 오류인지 찾으려고 ;;
        print(f"에러가 발생하였습니다. ({err})")
        msgbox.showerror("오류", f"오류가 발생하였습니다.\n{err}")


# 실행 프레임 >> 시작 버튼
start_btn = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
start_btn.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()