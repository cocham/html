#coding: euc-kr
import csv

#291
with open('매수종목1.txt','w',encoding='utf-8') as file:
    file.write('005930\n')
    file.write('005380\n')
    file.write('035420\n')

#292
with open('매수종목2.txt','w',encoding='utf-8') as file:
    l = ['005930 삼성전자','005380 현대차','035420 NAVER']
    for x in l:
        file.write(x+'\n')

#293
file_path = 'stock.csv'
data = [{"종목명":"삼성전자","종목코드":"005930","PER":15.79},
        {"종목명":"NAVER","종목코드":"035420","PER":55.82}
        ]

with open(file_path,'w',encoding = "utf-8", newline='') as file:
    headers = data[0].keys()
    csv_writer = csv.DictWriter(file,fieldnames=headers)

    csv_writer.writeheader()
    csv_writer.writerows(data)

#294
with open('매수종목1.txt','r') as file:
    lines = file.readlines()

    codes = []
for line in lines:
    code = line.strip()
    codes.append(code)
print(codes)

#295
with open('매수종목2.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    data = {}

for line in lines:
    line = line.strip()
    k,v = line.split()
    data[k] = v

print(data)

#296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

#297
per = ["10.31", "", "8.00"]
new_per = []
for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)
print(new_per)

#298
def div(a,b):
    try:
        a/b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")

#299
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

#300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("success")
    finally:
        print("실수로 변환")