#-*- coding: euc-kr -*-
'''
<201>
def print_coin():    
    print("비트코인")
-------
<202>
print_coin() 
-------
for i in range(100): #203
    print_coin()
-------
def print_coins():   #204
    for i in range(100):
        print("비트코인")
--------
def print_with_smile(s):
    print(s+":D")
--------
<221>
def print_reverse(s):
    print(s[::-1])
--------
<222>
def print_score(arr):
    print(sum(arr)/len(arr))
--------
<223>
def print_even(arr):
    for x in even:
        if x%2 == 0:
            print(x)
---------
<224>
def print_keys(dic):
    print(list(dic.keys()))
---------
<225>
def print_value_by_key(dic,day_k):
    my_dict = {"10/26" : [100, 130, 100, 100],
            "10/27" : [10, 12, 10, 11]}
    print(my_dict['day_k'])
---------
<226>
def print_5xn(string):
    ans = [string[i:i+5] for i in range(0,len(string),5)]
    for x in ans:
        print(x)
---------
<227>
def print_mxn(string,n):
    ans = [string[i:i+n] for i in range(0,len(string),n)]
    for x in ans:
        print(x)
---------
<228>
def calc_monthly_salary(annual_salary):
    money = int(annual_salary / 12)
    return money
---------
<232>
def make_url(str):
    return ("www." + str + ".com")
---------
<233>
def make_list(str):
    return list(str)
---------
<234>
def pickup_even(arr):
    ans = []
    for n in even:
        if n%2 == 0:
            ans.append(n)
    return ans
---------
<235>
def convert_int(str):
    s = int(''.join(str.split(',')))
    # s = int(str.replace(',',''))
    return s
---------
<252>
class Human:
---------
<253>
areum = Human()
---------
<254~255>
class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def baby(self):
        print("응애응애")
    
    def who(self):
        print(f"이름: {self.name} 나이: {self.age} 성별: {self.sex}")

    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
---------
<256>
areum = Human("조아름",25,"여자")
areum.who()

areum.setInfo("조아름",25,"여자")
'''