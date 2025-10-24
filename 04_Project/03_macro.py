import pyautogui
import time

# 각 요소의 클릭 좌표를 미리 설정합니다. (실제 환경에 맞게 수정 필요)
pos_start_year = (935, 679)     # 시작년도 클릭 좌표
pos_start_month = (1065, 679)    # 시작월 클릭 좌표
pos_end_year = (1218, 679)       # 끝년도 클릭 좌표
pos_end_month = (1357, 679)      # 끝월 클릭 좌표
pos_search_btn = (1411, 916)     # 검색버튼 클릭 좌표
pos_download_btn = (1462, 975)   # 엑셀 파일 다운로드 좌표

def year_click(year):

    # 1. 시작년도 클릭 - 입력 - 엔터
    pyautogui.click(pos_start_year)
    time.sleep(0.2)
    pyautogui.typewrite(year)      # 년도 입력
    time.sleep(0.2)
    pyautogui.press('enter')

    # 32. 끝년도 클릭 - 입력 - 엔터
    pyautogui.click(pos_end_year)
    time.sleep(0.2)
    pyautogui.typewrite(year)      # 년도 입력
    time.sleep(0.2)
    pyautogui.press('enter')

def month_click(start_m, end_m):

    # 3. 시작월 클릭 - 입력 - 엔터
    pyautogui.click(pos_start_month)
    time.sleep(0.2)
    pyautogui.typewrite(start_m)        # 월 입력
    time.sleep(0.2)
    pyautogui.press('enter')

    # 4. 끝월 클릭 - 입력 - 엔터
    pyautogui.click(pos_end_month)
    time.sleep(0.2)
    pyautogui.typewrite(end_m)        # 월 입력
    time.sleep(0.2)
    pyautogui.press('enter')

def download():
    # 5. 검색버튼 클릭 - 5초 이상 대기
    pyautogui.click(pos_search_btn)
    time.sleep(3)

    # 6. 엑셀파일 다운로드 클릭 - 1초 대기 후 엔터
    pyautogui.click(pos_download_btn)
    time.sleep(1)
    pyautogui.press('enter')

years = ['2023','2024','2025']
month_pair=[('01','06'),('7','12')]

for year in years:
    # 클릭 좌표를 미리 입력 (예:input을 통해 직접 지정)
    print('각 버튼의 좌표를 마우스로 확인해서 아래에 입력하세요!')

    time.sleep(3)

    year_click(year)

    for start_m, end_m in month_pair:
        month_click(start_m, end_m)
        download()

    

print('매크로 작업이 완료되었습니다!')
