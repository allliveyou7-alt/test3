import streamlit as st
import re

# 사칙연산 함수
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "오류! 0으로 나눌 수 없습니다."
    return a / b

# 스트림릿 꾸미기
st.set_page_config(page_title="나만의 계산기", page_icon="🧮", layout="centered")

st.markdown("""
<div style='background-color:#fffae5; padding:24px; border-radius:16px;'>
    <h2 style='text-align:center; color:#0c326f;'>🧮 나만의 계산기에 오신 것을 환영합니다! 🧮</h2>
    <div style='font-size:18px; color:#444; text-align:center;'>
        <b>사용 가능한 연산:</b><br>
        1. 덧셈 (+)<br>
        2. 뺄셈 (-)<br>
        3. 곱셈 (*)<br>
        4. 나눗셈 (/)
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

st.write("---")

# 입력
expr = st.text_input("계산할 식을 입력하세요 (예: 1+3 / 15-3 / 12.5/5)", key="expr")

if expr:
    # 종료용 q는 무시(웹에서는 사용이 애매)
    if expr.lower().strip() == 'q':
        st.info("계산기를 종료하고 싶으신가요? 스트림릿에서는 종료 버튼이 별도로 없습니다.")
    else:
        match = re.match(r"^\s*([\-]?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*([\-]?\d+(?:\.\d+)?)\s*$", expr)
        if not match:
            st.error("입력 형식이 올바르지 않습니다. 예: 1+3")
        else:
            a = float(match.group(1))
            op = match.group(2)
            b = float(match.group(3))

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            elif op == '*':
                result = mul(a, b)
            elif op == '/':
                result = div(a, b)
            else:
                st.error("지원하지 않는 연산자입니다.")
                result = None

            if result is not None:
                st.success(f"**{a} {op} {b} = {result}**")

st.write("---")
st.markdown("<div style='color:#888;text-align:center;'>간단 사칙연산 계산기로 빠른 계산하세요! 😃</div>", unsafe_allow_html=True)