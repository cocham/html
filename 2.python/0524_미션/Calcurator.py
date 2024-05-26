#coding: euc-kr
import re

def calcurate(str):
    try:
        s = re.split(r'[/*+-]',str)
        if not s[0].isdigit() or not s[1].isdigit() or len(s) >= 3:
            raise ValueError
        stack = [x for x in str if not x.isdigit()]
        if  "+" in stack:
            return f"��: {int(s[0]) + int(s[1])}"
        if "/" in stack:
            if int(s[1]) == 0:
                raise ZeroDivisionError
            return f"��:{int(s[0]) / int(s[1])}"
        if "*" in stack:
            return f"��: {int(s[0]) * int(s[1])}"
        if "-" in stack:
            return f"��: {int(s[0]) - int(s[1])}"
        print("------------")
    except ValueError:
        return ("�Է� ����: ���ÿ� ���� ���� �ۼ��ϼ���")
    except ZeroDivisionError:
        return ("0���� ���� �� �����ϴ�")

while True:
    c = input("======\n    ������ �Է��ϼ���.\n**�����Ϸ��� 1�� �Է��ϼ���** \n------\n<����>: 1+2 8*7 4/2 1-8 \n[���ϱ�: + ����: - ���ϱ�: * ������: /]\n======\n")
    if len(c) == 1 and int(c) == 1:
        print("���� ����")
        break
    print(calcurate(c))