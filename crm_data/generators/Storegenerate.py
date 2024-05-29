#coding: euc-kr
import random
import csv

class Storegenerate:
    def store_generate(self):
        with open('stores.csv','r') as file:
            csvreader = csv.reader(file)
            self.csv_list_stores = [n[i] for n in csvreader for i in range(len(n))]
        with open('stores_address.csv','r') as file2:
            csvreader2 = csv.reader(file2)
            self.csv_list_stadress = [n[i] for n in csvreader2 for i in range(len(n))] 
        
        return [random.choice(self.csv_list_stores),random.choice(self.csv_list_stadress),random.randint(1,10)]
