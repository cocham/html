#coding: euc-kr
import random
import csv

class Namegenerator:
    def __init__(self):
        with open('names.csv','r',encoding='euc-kr') as file:
            csvreader = csv.reader(file)
            self.csv_list_names = [n[i] for n in csvreader for i in range(len(n))]
            
    def generate_name(self):
        return random.choice(self.csv_list_names)


