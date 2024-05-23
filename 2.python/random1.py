# -*- coding: euc-kr -*-
import random
import string

# 미션1. 랜덤 숫자 1~100까지를 생성하는 함수를 찾아서 출력하시오.
def randomnum():
    return random.randrange(1,101)

# 미션2. 주사위를 던지는 함수를 작성하시오.
def dice():
    n = random.randint(1,6)
    return n
    
num = dice()
print(f"주사위의 숫자는 {num}입니다.")

# 미션3. list에서 랜덤으로 요소를 선택하기
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
def choose_random_element(arr):
    return random.choice(arr)

f = choose_random_element(fruits)
print(f"랜덤으로 선택된 리스트 요소는 {f}입니다.")

# 미션4. 랜덤으로 리스트 섞기
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
nums = [i for i in range(1,11)]
def mix(arr):
    arr2 = random.sample(arr,k=len(arr)) #shuffle은 리턴값이 없어서 sample을 사용함.
    return arr2
'''
def mix(arr):
    random.shuffle(arr)
    return arr
'''

# 미션5. 랜덤으로 문자열 생성 (영문 대문자 6자리)
def randomstring():
    s = ''
    for i in range(6):
        s += str(random.choice(string.ascii_uppercase))
    return s
print(randomstring())

# 미션6. 랜덤 초이스에서 가중치를 고려한 랜덤
def randomchoice(arr):
    weights = [0.15,0.4,0.5,0.21,0.34,0.84]
    return random.choices(arr,weights)
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
print(randomchoice(fruits))

# 미션7. 랜덤 비밀번호 생성(대소문자, 숫자포함 8자리)
def randomstring():
    s = ''
    for i in range(8):
        s += str(random.choice(string.ascii_letters + string.digits))
    return s
print(randomstring())

# 미션8. 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리를 만드려면? )
def randomNum():
    return str(random.randint(1,9))

def randomLower():
    return str(random.choice(string.ascii_lowercase))

def randomUpper():
    return str(random.choice(string.ascii_uppercase))

def must_randomstring():
    must = []
    must.extend([randomNum(),randomLower(),randomUpper()]) #조건 만족
    random.shuffle(must)
    s = ''.join(must)
    for i in range(5):
        s += str(random.choice(string.ascii_letters + string.digits)) #나머지 5자리 완성
    s = random.sample(s,k=len(s)) #must+새로 생성된5자리 꼴이므로 한 번 더 섞음
    return ''.join(s)

print(must_randomstring())