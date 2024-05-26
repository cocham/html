#coding: euc-kr

info = []
def score_game():
    while True:
        try:
            print("=======")
            menu = input("��带 �Է��ϼ���(high/score/history/q(����))\n")
            if menu not in ["high","score","history","q"]:
                raise KeyError
            print("-------")
            if menu == "score":
                user_n = input("�̸��� �Է��ϼ���: ")
                user_s = input("������ �Է��ϼ���: ")
                if user_s in ["0","-0","+0"]:
                    user_s = 0
                elif user_s[0] == '-' or user_s[0] == '+': #��ȣ�� �پ����� ���
                        user_s = float(user_s)
                elif not user_s.isdigit():
                    raise ValueError
                else:
                    user_s = float(user_s)
                info.extend([[user_n,user_s]])

            if menu == "q":
                print("��������")
                break

            if menu == "high":
                if len(info) == 0:
                    print("������ �������� �ʽ��ϴ�")
                else:
                    print(f"�ְ� ����: {max([x[1] for x in info])}")
            
            if menu == "history":
                if len(info) == 0:
                    print("���� ����� �������� �ʽ��ϴ�")
                else:
                    print(f"���� ���: {info}")
            
        except KeyError:
            print("�޴� ����: �ùٸ� �޴��� �Է��ϼ���")
        except ValueError:
            print("���� ����: �ùٸ� ���ڸ� �Է��ϼ���")

score_game()