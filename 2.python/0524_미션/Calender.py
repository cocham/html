#coding: euc-kr
#그레고리력(1583~)

'''
[사용 로직]
특정 년도의 1월 1일의 요일에서 그 다음 년도의 1월 1일의 요일은 평년일 때 1일, 윤년일 때 2일 오른쪽으로 이동한다.
특정 월의 1일의 요일에서 그 다음 월의 1일의 요일은 해당 월의 총 일수를 7로 나눈 나머지만큼 오른쪽으로 이동한다.
'''
def isleap(y):
    if y%4 == 0 and y%100 != 0 or y % 400 == 0:
        return 0 #윤년
    else:
        return 1

def first_day(y,m): #해당년도의 1월 1일 요일 계산
    s = 0
    for x in range(1583,y): #1583.01.01 = saturday(6)
        if isleap(x) == 0:
            s += 2
        else:
            s += 1
    return (s+6)%7 #일~월 인덱스는 0~6
        
def month_first_day(y,m): #해당월의 1일 요일 계산
    m1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    m2 = [31,29,31,30,31,30,31,31,30,31,30,31]
    s_d = first_day(y,m) 
    if isleap(y) == 0: #윤년
        total_d = m2[m-1]
        for i in range(1,m): #1월부터 m까지
            p_m = m2[i-1]%7 #previous month의 첫날 요일 계산
            s_d += p_m #오른쪽으로 이동
    else:
        total_d = m1[m-1]
        for i in range(1,m): #1월부터 m까지
            p_m = m1[i-1]%7
            s_d += p_m
    return s_d %7

def calc_month(y,m):
    return [31,29,31,30,31,30,31,31,30,31,30,31] if isleap(y) == 0 else [31,28,31,30,31,30,31,31,30,31,30,31]

def print_calender(y,m):
    print('='*28)
    print(f"         {y}년 {m}월")
    print('='*28)
    print("Sun Mon Tue Wed Thu Fri Sat")
    print('='*28)

    t = calc_month(y,m)
    num = [i for i in range(1,t[m-1]+1)]
    s_i = month_first_day(y,m) #start_index
    for i in range(s_i):
        print("    ",end = '')
    for x in num:
        print(' {0:2d} '.format(x),end = '')
        s_i += 1
        if s_i % 7 == 0:
            print('\n')

    print('\n'+'='*28)    

while True:
    year = int(input("년도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))
    print_calender(year,month)