# -*- coding: euc-kr -*-
'''
<3>
print('�ž��� �Ҹ�������. "�����̾�".')
--------
<11>
�Ｚ���� = 50000
���򰡱ݾ� = �Ｚ���� * 10
print(���򰡱ݾ�)
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
license_plate = "24�� 2210"
print(license_plate[-4:])
--------
<23>
string = "Ȧ¦Ȧ¦Ȧ¦"
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
name1 = "��μ�" 
age1 = 10
name2 = "��ö��"
age2 = 13

print('�̸�: {} ����: {}'.format(name1,age1))
print(f"�̸�: {name2} ����: {age2}")
print('�̸�: %s ����: %d' %(name1,age1))
--------
<38>
�����ֽļ� = "5,969,782,550"
�����ֽļ� = �����ֽļ�.replace(',','')
print(int(�����ֽļ�))
--------
<39>
�б� = "2020/03(E) (IFRS����)"
print(�б�[:7])
--------
<40>
data = "   �Ｚ����    "
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
file_name = "����.xlsx"
file_name.endswith("xlsx")
--------
<45>
file_name = "����.xlsx"
file_name.endswith(("xlsx","xls"))
--------
<46>
file_name = "2020_����.xlsx"
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
movie_rank = ['���� ��Ʈ������', '���ø�', '��Ű', '��Ʈ��']
movie_rank.insert(1,'���۸�')
--------
<54>
movie_rank.remove('��Ű')
del movie_rank[3]
--------
<55>
movie_rank = ['���� ��Ʈ������', '���۸�', '���ø�', '��Ʈ��']
movie_rank2 = [m for m in movie_rank if m!= '���ø�' and m!= '��Ʈ��']


'''








'''