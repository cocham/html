# -*- coding: euc-kr -*-
import random
import string

# �̼�1. ���� ���� 1~100������ �����ϴ� �Լ��� ã�Ƽ� ����Ͻÿ�.
def randomnum():
    return random.randrange(1,101)

# �̼�2. �ֻ����� ������ �Լ��� �ۼ��Ͻÿ�.
def dice():
    n = random.randint(1,6)
    return n
    
num = dice()
print(f"�ֻ����� ���ڴ� {num}�Դϴ�.")

# �̼�3. list���� �������� ��Ҹ� �����ϱ�
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
def choose_random_element(arr):
    return random.choice(arr)

f = choose_random_element(fruits)
print(f"�������� ���õ� ����Ʈ ��Ҵ� {f}�Դϴ�.")

# �̼�4. �������� ����Ʈ ����
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
nums = [i for i in range(1,11)]
def mix(arr):
    arr2 = random.sample(arr,k=len(arr)) #shuffle�� ���ϰ��� ��� sample�� �����.
    return arr2
'''
def mix(arr):
    random.shuffle(arr)
    return arr
'''

# �̼�5. �������� ���ڿ� ���� (���� �빮�� 6�ڸ�)
def randomstring():
    s = ''
    for i in range(6):
        s += str(random.choice(string.ascii_uppercase))
    return s
print(randomstring())

# �̼�6. ���� ���̽����� ����ġ�� ����� ����
def randomchoice(arr):
    weights = [0.15,0.4,0.5,0.21,0.34,0.84]
    return random.choices(arr,weights)
fruits = ["apple","cherry","banana","melon","pineapple","grape"]
print(randomchoice(fruits))

# �̼�7. ���� ��й�ȣ ����(��ҹ���, �������� 8�ڸ�)
def randomstring():
    s = ''
    for i in range(8):
        s += str(random.choice(string.ascii_letters + string.digits))
    return s
print(randomstring())

# �̼�8. ������ ��й�ȣ ���� (�빮��, �ҹ���, ���ڸ� ���� �ּ� 1���̻� �����ϴ� 8�ڸ��� �������? )
def randomNum():
    return str(random.randint(1,9))

def randomLower():
    return str(random.choice(string.ascii_lowercase))

def randomUpper():
    return str(random.choice(string.ascii_uppercase))

def must_randomstring():
    must = []
    must.extend([randomNum(),randomLower(),randomUpper()]) #���� ����
    random.shuffle(must)
    s = ''.join(must)
    for i in range(5):
        s += str(random.choice(string.ascii_letters + string.digits)) #������ 5�ڸ� �ϼ�
    s = random.sample(s,k=len(s)) #must+���� ������5�ڸ� ���̹Ƿ� �� �� �� ����
    return ''.join(s)

print(must_randomstring())