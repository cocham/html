#coding: euc-kr
import random
import csv
import uuid
from datetime import datetime, timedelta

# StoreId,UserId�� csv���Ͽ��� �о�;ߵ�.

class Ordergenerator:
    def read_user(self):
        u = []
        with open('output_user.csv','r') as file:
            freader = csv.reader(file)
            next(freader) #�������
            for row in freader:
                u.append(row[0])
        return u
    
    def read_store(self):
        s = []
        with open('output_store.csv','r') as file:
            freader = csv.reader(file)
            next(freader) #�������
            for row in freader:
                s.append(row[0])
        return s

    def order_generate(self):
        st = datetime(2023,1,1)
        et = datetime(2024,5,1)
        rt = random.randint(0,(et-st).total_seconds())
        id = str(uuid.uuid4())
        order_at = str(st + timedelta(seconds = rt))
        user_id = random.choice(self.read_user())
        store_id = random.choice(self.read_store())
        order = (id,order_at,user_id,store_id)
        return order
