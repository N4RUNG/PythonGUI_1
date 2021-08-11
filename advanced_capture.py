from PIL import ImageGrab # 이미지 캡쳐
import keyboard # 키보드 입력 감지
import time # 파일 이름 시간으로 저장

def screenshot():
    img = ImageGrab.grab()
    img.save(time.strftime("%Y%m%d%H%M%S.png"))

keyboard.add_hotkey("F9", screenshot) # F9 를 누르면 screenshot 수행
# keyboard.add_hotkey("ctrl+shift+s", screenshot) # ctrl, shift, s 를 누르면 screenshot 수행 ( 다중 입력 )
keyboard.wait("esc") # esc 를 누를 때까지 프로그램 수행 ( esc를 누르면 프로그램이 꺼짐 ) ( break 포인트 )