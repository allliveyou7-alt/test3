import streamlit as st
import random
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = 'OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw'
endpoint = 'https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6'

# ⚠️ 반드시 네이버 개발자에서 발급받은 영문/숫자 값으로 교체!
NAVER_CLIENT_ID = 'YOUR_CLIENT_ID'    # 예시: 'ZFmGvAtJ7kBx'
NAVER_CLIENT_SECRET = 'YOUR_CLIENT_SECRET' # 예시: 'B5gJe5dY0S'

HOESIK_MENUS = [
    "삼겹살", "치킨", "곱창", "회", "목살", "닭갈비", "쭈꾸미", "돼지갈비", "중국집", "일식집",
    "파스타", "피자", "냉면", "양꼬치", "홍합찜", "해물탕", "고깃집", "버거", "초밥", "분식",
    "감자탕", "족발", "곰탕", "부대찌개", "맥주집", "포장마차", "닭도리탕", "불백", "오리구이"
]

def naver_search(query, display=3):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        'X-Naver-Client-Id': NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
    }
    params = {
        'query': query,  # 한글 가능! (requests가 알아서 처리함)
        'display': display,
        'sort': 'sim'
    }
    resp = requests.get(url, headers=headers, params=params, verify=False)
    if resp.status_code != 200:
        return f"[네이버뉴스 API 에러] {resp.status_code}: {resp.text}"
    try:
        items = resp.json().get('items', [])
        result = ""
        for idx, item in enumerate(items):
            title = re.sub("<.*?>", "", item['title'])
            desc = re.sub("<.*?>", "", item['description'])
            link = item['link']
            result += f"{idx+1}. {title}\n- 요약: {desc}\n- 링크: {link}\n"
        return result.strip() or "검색 결과가 없습니다."
    except Exception as e:
        return f"네이버 뉴스 파싱 오류: {str(e)}"

def get_ai_answer(messages):
    url = endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "messages": messages
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, verify=False)
        if resp.status_code == 200:
            json_resp = resp.json()
            return json_resp.get("answer", "응답 파싱 오류입니다.")
        else:
            return f"API 오류: {resp.status_code}, {resp.text}"
    except Exception as e:
        return f"API 호출 실패: {e}"

if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 실시간 뉴스와 챗봇으로 도와드릴게요."}
    ]
if "chat_list" not in st.session_state:
    st.session_state["chat_list"] = []
if "email_mode" not in st.session_state:
    st.session_state["email_mode"] = False
if "hoesik_menu" not in st.session_state:
    st.session_state["hoesik_menu"] = None
if "otaku_mode" not in st.session_state:
    st.session_state["otaku_mode"] = False

with st.sidebar:
    st.header("🍽️ 회식 메뉴 랜덤 추천")
    if st.button("오늘 회식 뭐 먹을까?", use_container_width=True, key="hoesik_btn"):
        st.session_state["hoesik_menu"] = random.choice(HOESIK_MENUS)
    if st.session_state["hoesik_menu"]:
        st.success(f"✅ 오늘 추천 메뉴: **{st.session_state['hoesik_menu']}**", icon="🍽️")

    st.markdown("---")
    st.subheader("🕹️ 오타쿠 모드")
    st.session_state["otaku_mode"] = st.toggle("오타쿠 말투로 답변하기", key="otaku_mode_toggle")

    st.markdown("---")
    st.subheader("🧾 메일(이메일 양식) 모드")
    if st.button("메일 모드 토글", key="email_toggle_btn"):
        st.session_state["email_mode"] = not st.session_state["email_mode"]
    if st.session_state["email_mode"]:
        st.info("✉️ 메일 형식으로 답변합니다.", icon="📧")

    st.markdown("---")
    st.subheader("💬 새로운 채팅")
    if st.button("새로운 채팅", use_container_width=True, key="newchat_btn"):
        if len(st.session_state["history"]) > 1:
            last_user = next((m["content"] for m in reversed(st.session_state["history"]) if m["role"]=="user"), "질문 없음")
            last_assist = next((m["content"] for m in reversed(st.session_state["history"]) if m["role"]=="assistant"), "답변 없음")
            st.session_state["chat_list"].append(
                f"Q: {last_user[:30]}... / A: {last_assist[:30]}..."
            )
        st.session_state["history"] = [
            {"role": "assistant", "content": "새로운 대화를 시작합니다! 무엇이든 물어보세요."}
        ]

    st.markdown("---")
    st.subheader("🗂️ 이전 대화 기록 리스트")
    if st.session_state["chat_list"]:
        for i, c in enumerate(reversed(st.session_state["chat_list"])):
            st.caption(f"{i+1}. {c}")
    else:
        st.info("저장된 이전 대화가 없습니다.", icon="🗒️")
    st.markdown("---")
    st.caption("사이드바에서 각종 기능을 활용해보세요!")

st.set_page_config(page_title="실시간 뉴스 챗봇", page_icon="🌐", layout="wide")
st.title("🌐 실시간 네이버 뉴스 챗봇 (실습/테스트용)")

user_input = st.chat_input("질문을 입력하세요.")

if user_input:
    st.session_state["history"].append({"role": "user", "content": user_input})

    news_result = naver_search(user_input)
    search_info = f"\n[실시간 뉴스]\n{news_result}"

    otaku_prompt = ""
    if st.session_state["otaku_mode"]:
        otaku_prompt = (
            "그리고 반드시 오타쿠 말투(흔한 일본 애니메이션의 열정적·과몰입 말투, '~입니다! '~이군요!', '~인거에요!' 등)로 답해줘! "
            "어색한 단어나 말 끝에 감탄사(머쓱, 쿄쿄, 운다, 우왓 등)도 섞어줘. 일본식 말투 느낌으로 부탁해요!!"
        )
    email_prompt = ""
    if st.session_state["email_mode"]:
        email_prompt = (
            "추가 지시: 답변을 꼭 회사 업무용 메일 양식으로 써줘! 인사말, 끝 인사 포함! "
        )

    system_content = (
        f"사용자 질문과 아래 실시간 뉴스 결과를 참고해서 최신 뉴스/정보를 반영해서 답변하세요. "
        f"{email_prompt}{otaku_prompt}\n{search_info}"
    )
    system_prompt = {"role": "system", "content": system_content}
    chat_messages = [system_prompt] + st.session_state["history"]

    answer = get_ai_answer(chat_messages)
    st.session_state["history"].append({"role": "assistant", "content": answer})

for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

st.markdown("---")
st.info("(실습/테스트용입니다. 배포시 SSL 검증을 반드시 켜주세요!)", icon="🔒")
