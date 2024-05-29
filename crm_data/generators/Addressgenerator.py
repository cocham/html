#coding: euc-kr
import random
import csv

class Addressgenerate:
    def addressgenerate(self):
        with open ('residence.csv','r') as file:
            csvreader = csv.reader(file)
            self.csv_list_cities = [n[i] for n in csvreader for i in range(len(n))] 

        self.n = ['대로','로','길']
        return f"{random.choice(self.csv_list_cities)} {random.randint(1,100)}{random.choice(self.n)} {random.randint(1,100)}"