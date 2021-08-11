from PIL import ImageGrab
import time

time.sleep(5) # 5초 대기 시간

for i in range(1, 11): # 1~10번
    img = ImageGrab.grab() # 이미지 캡쳐
    img.save(f"Image{i}.png") # 이미지를 번호와 함께 저장
    time.sleep(2) # 2초 대기