#coding: euc-kr

info = []
def score_game():
    while True:
        try:
            print("=======")
            menu = input("모드를 입력하세요(high/score/history/q(종료))\n")
            if menu not in ["high","score","history","q"]:
                raise KeyError
            print("-------")
            if menu == "score":
                user_n = input("이름을 입력하세요: ")
                user_s = input("점수를 입력하세요: ")
                if user_s in ["0","-0","+0"]:
                    user_s = 0
                elif user_s[0] == '-' or user_s[0] == '+': #기호가 붙어있을 경우
                        user_s = float(user_s)
                elif not user_s.isdigit():
                    raise ValueError
                else:
                    user_s = float(user_s)
                info.extend([[user_n,user_s]])

            if menu == "q":
                print("게임종료")
                break

            if menu == "high":
                if len(info) == 0:
                    print("점수가 존재하지 않습니다")
                else:
                    print(f"최고 점수: {max([x[1] for x in info])}")
            
            if menu == "history":
                if len(info) == 0:
                    print("게임 기록이 존재하지 않습니다")
                else:
                    print(f"게임 기록: {info}")
            
        except KeyError:
            print("메뉴 에러: 올바른 메뉴를 입력하세요")
        except ValueError:
            print("점수 에러: 올바른 숫자를 입력하세요")

score_game()