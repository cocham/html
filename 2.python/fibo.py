#-*- coding: euc-kr-*-
#한글 깨짐 수정
def fibo(num):
    a,b = 1,1
    n = a+b
    l = [a,b,n]

    while True:
        a = b
        b = n
        n = a+b
        l.append(n)
        if len(l)>=num:
            break
    return l

num = int(input("피보나치 수열 개수 입력: "))
print(fibo(num))
