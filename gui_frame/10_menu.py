from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

menu1 = Menu(root)
menu_file = Menu(menu1, tearoff=0) # menu1 안에 넣을 파일

# File
def new():
    print("새 파일을 만듭니다.")
menu_file.add_command(label="New File", command=new)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분선
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save")
menu_file.add_command(label="Save As...")
menu_file.add_command(label="Save All", state="disable") # 비활성화 된 버튼
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu1.add_cascade(label="File", menu=menu_file)

# Edit
menu1.add_cascade(label="Edit") # 아무것도 없는 메뉴

# Language (라디오 버튼)
menu_lang = Menu(menu1, tearoff=0)
menu_lang.add_radiobutton(label="Korean")
menu_lang.add_radiobutton(label="English")
menu_lang.add_radiobutton(label="Russian")
menu1.add_cascade(label="Language", menu=menu_lang)

# View (체크 버튼)
menu_view = Menu(menu1, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu1.add_cascade(label="View", menu=menu_view)

root.config(menu=menu1) # menu= 로 메뉴 설정
root.mainloop()