import re

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

print("        ========================================")
print("        🧮 나만의 계산기에 오신 것을 환영합니다! 🧮")
print()
print("        사용 가능한 연산:")
print("        1. 덧셈 (+)")
print("        2. 뺄셈 (-)")
print("        3. 곱셈 (×)")
print("        4. 나눗셈 (÷)")
print()
print("        ========================================")

while True:
    expr = input("계산할 식을 입력하세요 (예: 1+3, 종료는 q): ")
    if expr.lower().strip() == 'q':
        break

    # 정규표현식으로 숫자와 연산자를 분리 (예: 15+3, 2.5*9)
    match = re.match(r"^\s*([\-]?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*([\-]?\d+(?:\.\d+)?)\s*$", expr)
    if not match:
        print("입력 형식이 올바르지 않습니다. 예: 1+3")
        continue

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
        print("지원하지 않는 연산자입니다.")
        continue

    print(f"{a} {op} {b} = {result}")

print("계산기를 사용해주셔서 감사합니다!")