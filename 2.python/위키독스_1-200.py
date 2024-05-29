# -*- coding: euc-kr -*-
'''
<3>
print('신씨가 소리질렀다. "도둑이야".')
--------
<11>
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
--------
<13>
s = "hello"
t = "python"
print(s+'!',t)
--------
<21>
letters = 'python'
print(letters[0],letters[2])
--------
<21>
license_plate = "24가 2210"
print(license_plate[-4:])
--------
<23>
string = "홀짝홀짝홀짝"
print(string[::2])
--------
<24>
string = "PYTHON"
print(string[::-1])
--------
<25>
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))
--------
<26>
phone_number = "010-1111-2222"
print(phone_number.replace('-',''))
--------
<27>
url = "http://sharebook.kr"
print(url.split('.')[-1])
--------
<29>
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)

/* l = []
for x in string:
    if x == 'a':
        l.append('A')
    else:
        l.append(x)
return ''.join(l) */
--------
<34>
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' ' 

print(t3*4)
--------
<35>
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print('이름: {} 나이: {}'.format(name1,age1))
print(f"이름: {name2} 나이: {age2}")
print('이름: %s 나이: %d' %(name1,age1))
--------
<38>
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',','')
print(int(상장주식수))
--------
<39>
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
--------
<40>
data = "   삼성전자    "
data1 = data.strip()
print(data1)
--------
<41>
ticker = "btc_krw"
print(ticker.upper())
--------
<42>
ticker = "BTC_KRW"
print(ticker.lower())
--------
<43>
s = 'hello'
s = s.capitalize()
--------
<44>
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
--------
<45>
file_name = "보고서.xlsx"
file_name.endswith(("xlsx","xls"))
--------
<46>
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
--------
<47>
a = "hello world"
a.split()
--------
<48>
ticker = "btc_krw"
ticker.split("_")
--------
<49>
date = "2020-05-01"
date.split("-")
--------
<50>
data = "039490     "
data = data.rstrip()
--------
<53>
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')
--------
<54>
movie_rank.remove('럭키')
del movie_rank[3]
--------
<55>
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank2 = [m for m in movie_rank if m!= '스플릿' and m!= '배트맨']


'''








'''