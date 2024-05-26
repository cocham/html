#coding: euc-kr
import re

def calcurate(str):
    try:
        s = re.split(r'[/*+-]',str)
        if not s[0].isdigit() or not s[1].isdigit() or len(s) >= 3:
            raise ValueError
        stack = [x for x in str if not x.isdigit()]
        if  "+" in stack:
            return f"답: {int(s[0]) + int(s[1])}"
        if "/" in stack:
            if int(s[1]) == 0:
                raise ZeroDivisionError
            return f"답:{int(s[0]) / int(s[1])}"
        if "*" in stack:
            return f"답: {int(s[0]) * int(s[1])}"
        if "-" in stack:
            return f"답: {int(s[0]) - int(s[1])}"
        print("------------")
    except ValueError:
        return ("입력 오류: 예시와 같이 식을 작성하세요")
    except ZeroDivisionError:
        return ("0으로 나눌 수 없습니다")

while True:
    c = input("======\n    계산식을 입력하세요.\n**종료하려면 1을 입력하세요** \n------\n<예시>: 1+2 8*7 4/2 1-8 \n[더하기: + 빼기: - 곱하기: * 나누기: /]\n======\n")
    if len(c) == 1 and int(c) == 1:
        print("계산기 종료")
        break
    print(calcurate(c))