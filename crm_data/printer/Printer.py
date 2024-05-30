#coding: euc-kr
import csv

class Printer:
    def print_to_screen(d_type,d_list):
        if d_type in ["user","store","item","order","orderitem"]:
            for d in d_list:
                print(d)
                
    def print_to_file(d_type,d_list):
        if d_type == "user":
            with open('output_user.csv','w',encoding = 'euc-kr',newline='') as file:
                        fwriter = csv.writer(file)
                        headers = ["id", "name", "gender", "age", "birthday","address"]
                        file.write(",".join(headers)+'\n')
                        for x in d_list:
                            fwriter.writerows(x)    

        elif d_type == "store":
            with open('output_store.csv','w',encoding = 'euc-kr',newline='') as file:
                        fwriter = csv.writer(file)
                        headers = ["id", "name", "gender", "age", "birthday","address"]
                        file.write(",".join(headers)+'\n')
                        for x in d_list:
                            fwriter.writerows(x)    

        elif d_type == "item":
            with open('output_item.csv','w',encoding = 'euc-kr',newline='') as file:
                        fwriter = csv.writer(file)
                        headers = ["id", "name", "gender", "age", "birthday","address"]
                        file.write(",".join(headers)+'\n')
                        for x in d_list:
                            fwriter.writerows(x)

        elif d_type == "order":
            with open('output_order.csv','w',encoding = 'euc-kr',newline='') as file:
                fwriter = csv.writer(file)
                headers = ['Id','OrderAt','StoreId','UserId']
                file.write(','.join(headers)+'\n')
                for x in d_list:
                    fwriter.writerows(x)

        elif d_type == "orderitem":
            with open('output_orderitem.csv','w',encoding = 'euc-kr',newline='') as file:
                fwriter = csv.writer(file)
                headers = ['Id','OrderId','ItemId']
                file.write(','.join(headers)+'\n')
                for x in d_list:
                    fwriter.writerows(x)        