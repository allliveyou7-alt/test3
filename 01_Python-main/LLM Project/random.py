import streamlit as st
import random

# 창원 현대위아 근처 맛집 상호명 + 대표 아이콘 (예시)
restaurants = [
    ("진우정", "🍲"),
    ("마산아구할매", "🐟"),
    ("전주식당", "🍚"),
    ("곤지암소머리국밥", "🍖"),
    ("농민순대국", "🥓"),
    ("왕돼지국밥", "🐷"),
    ("불막창", "🔥"),
    ("한끼식당", "🥢"),
    ("창원참숯불갈비", "🥩"),
    ("가마솥양푼이족발", "🐾"),
    ("홍콩반점", "🍜"),
    ("청운루", "🥡"),
    ("모모스시", "🍣"),
    ("남산돈까스", "🍱"),
    ("떡꼬치네", "🍢"),
    ("버거파크", "🍔"),
    ("브런치&커피 라움", "☕"),
    ("지오벨라", "🍕"),
    ("타이완쌀국수", "🍲"),
    ("할리스커피 창원성산점", "🧋"),
]

st.set_page_config(page_title="창원 현대위아 회식 맛집 추천", page_icon="🍻", layout="centered")

# 헤더 영역 꾸미기
st.markdown(
    """
    <style>
    .title {font-size:2.4em; font-weight:bold; color:#0c326f;}
    .sub {font-size:1.08em; color:#444;}
    .bgimg {
        background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80');
        background-size: cover;
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="bgimg"><div class="title">🍻 창원 현대위아 <br>회식 장소 랜덤 추천! 🍣🍕🍖</div><div class="sub">오늘의 분위기는 어디서 만들어볼까요? <br>원클릭으로 회식 맛집을 추천받으세요!</div></div>', unsafe_allow_html=True)

st.write('---')

# 선택한 식당 출력
if st.button("🎲 오늘의 회식 맛집 추천받기!"):
    restaurant, icon = random.choice(restaurants)
    st.balloons()
    st.markdown(f"""
    <div style="text-align:center;">
        <span style="font-size:55px;">{icon}</span><br>
        <span style="font-size:2.3em; font-weight:bold; color:#f06543;">{restaurant}</span><br>
    </div>
    """, unsafe_allow_html=True)
    st.success("축하합니다! 회식 장소가 결정되었습니다 🎉")

else:
    st.info("아래 버튼을 눌러 오늘의 추천 회식 장소를 알아보세요!")

# 맛집 전체 리스트도 함께 보여주기
with st.expander("📒 창원 현대위아 근처 전체 맛집 리스트 보기"):
    st.markdown('<ul>' + ''.join([f'<li style="font-size:1.1em;">{icon} {restaurant}</li>' for restaurant, icon in restaurants]) + '</ul>', unsafe_allow_html=True)

# 꼬릿말
st.write("---")
st.markdown(
    "<div style='font-size:0.95em; color:#888;'>직장인들의 회식 장소 고민을 한방에!<br>모임/동료와 맛있는 창원 생활 되세요 🎈</div>",
    unsafe_allow_html=True
)