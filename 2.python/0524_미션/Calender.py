#coding: euc-kr
#�׷�����(1583~)

'''
[��� ����]
Ư�� �⵵�� 1�� 1���� ���Ͽ��� �� ���� �⵵�� 1�� 1���� ������ ����� �� 1��, ������ �� 2�� ���������� �̵��Ѵ�.
Ư�� ���� 1���� ���Ͽ��� �� ���� ���� 1���� ������ �ش� ���� �� �ϼ��� 7�� ���� ��������ŭ ���������� �̵��Ѵ�.
'''
def isleap(y):
    if y%4 == 0 and y%100 != 0 or y % 400 == 0:
        return 0 #����
    else:
        return 1

def first_day(y,m): #�ش�⵵�� 1�� 1�� ���� ���
    s = 0
    for x in range(1583,y): #1583.01.01 = saturday(6)
        if isleap(x) == 0:
            s += 2
        else:
            s += 1
    return (s+6)%7 #��~�� �ε����� 0~6
        
def month_first_day(y,m): #�ش���� 1�� ���� ���
    m1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    m2 = [31,29,31,30,31,30,31,31,30,31,30,31]
    s_d = first_day(y,m) 
    if isleap(y) == 0: #����
        total_d = m2[m-1]
        for i in range(1,m): #1������ m����
            p_m = m2[i-1]%7 #previous month�� ù�� ���� ���
            s_d += p_m #���������� �̵�
    else:
        total_d = m1[m-1]
        for i in range(1,m): #1������ m����
            p_m = m1[i-1]%7
            s_d += p_m
    return s_d %7

def calc_month(y,m):
    return [31,29,31,30,31,30,31,31,30,31,30,31] if isleap(y) == 0 else [31,28,31,30,31,30,31,31,30,31,30,31]

def print_calender(y,m):
    print('='*28)
    print(f"         {y}�� {m}��")
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
    year = int(input("�⵵�� �Է��ϼ���: "))
    month = int(input("���� �Է��ϼ���: "))
    print_calender(year,month)