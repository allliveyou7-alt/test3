import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # 마우스의 현재 좌표 얻기
        print(f"현재 마우스 위치: x={x}, y={y}")
        time.sleep(0.1)  # 0.1초 대기 (초당 10번 출력)
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")