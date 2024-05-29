#coding: euc-kr
import csv
from generators.Usergenerator import DataGenerator
from generators.Storegenerator import Datagenerator_store
from generators.Itemgenerator import Datagerator_item
from generators.Ordergenerator import Ordergenerator
from generators.OrderItemgenerator import OrderItem
from printer.Printer import Printer

def generate_u(numbers):
    u = DataGenerator(int(numbers))
    user = u.generate_users() #generate_users()���� for���� ���ư�.
    return user      

def generate_s(numbers):
    s = Datagenerator_store(int(numbers))
    store = s.generate_stores()
    return store

def generate_i(numbers):
    i = Datagerator_item(int(numbers))
    item = i.generate_item()
    return item

def generate_o(numbers):
    l = []
    for i in range(numbers):
        o = Ordergenerator()
        b = o.order_generate()
        l.append(b)
    return l

def generate_oi(numbers):
    l = []
    for i in range(numbers):
        oi = OrderItem()
        b = oi.orderitem_generate()
        l.append(b)
    return l


if __name__ == "__main__":
    menu = input("[������ ������(user | store | item | order | orderitem), ����, ��� ���]�� �Է��ϼ���(�������� ����)\n[��� ��� �ɼ�: ��ũ��/����]\n")
    d_type = menu.split()[0]
    n = menu.split()[1]
    show = menu.split()[2]
    
    if d_type.lower() == "user":
        ans = generate_u(int(n))
        s = Printer
        if show == "��ũ��":
            s.print_to_screen(d_type,ans)
        elif show == "����":
            s.print_to_file(d_type,[ans])
    
    elif d_type.lower() == "store":
        ans = generate_s(int(n))
        s = Printer
        if show == "��ũ��":
            s.print_to_screen(d_type,ans)
        elif show == "����":
            s.print_to_file(d_type,[ans])
    
    elif d_type.lower() == "item":
        ans = generate_i(int(n))
        s = Printer
        if show == "��ũ��":
            s.print_to_screen(d_type,ans)
        elif show == "����":
            s.print_to_file(d_type,[ans])

    elif d_type.lower() == "order":
        ans = generate_o(int(n))
        s = Printer
        if show == "��ũ��":
            s.print_to_screen(d_type,ans)
        elif show == "����":
            s.print_to_file(d_type,[ans])

    elif d_type.lower() == "orderitem":
        ans = generate_oi(int(n))
        s = Printer
        if show == "��ũ��":
            s.print_to_screen(d_type,ans)
        elif show == "����":
            s.print_to_file(d_type,[ans])