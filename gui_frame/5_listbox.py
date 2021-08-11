from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

listbox1 = Listbox(root, selectmode="extended", height=0)
# selectmode= 에서 "extended" 를 하면 여러 개 선택 가능
# selectmode= 에서 "single" 을 하면 한 개만 선택 가능
# height= 에 0을 적으면 리스트에 있는 모두를 보여주고, 숫자를 적으면 그 숫자의 개수만큼만 보여줌.
listbox1.insert(0, "Python")
listbox1.insert(1, "Java")
listbox1.insert(2, "JavaScript")
listbox1.insert(END, "C#") # 어차피 뒤에다 추가하는 것이므로 END를 적어도 무방함.
listbox1.insert(END, "C++")
listbox1.pack()

def btcmd():
    # 삭제
    listbox1.delete(END) # 가장 뒤 항목을 삭제

    # 개수 확인
    print(f"리스트에는 {listbox1.size()} 개가 있습니다.") # .size() 는 개수 확인
    
    # 항목 확인
    print(f"첫 번째부터 세 번째까지의 항목 : {listbox1.get(0, 2)}") # .get() 은 항목을 가져옴.

    # 선택 항목 확인
    print(f"선택된 항목 : {listbox1.curselection()}") # curselection() 은 커서로 선택한 항목의 idx 값을 가져옴
button1 = Button(root, text="버튼1", command=btcmd)
button1.pack()

root.mainloop()