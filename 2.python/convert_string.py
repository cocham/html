#coding: euc-kr -*-
#���ڸ� �Է¹޾�, ��ҹ��ڸ� �����Ͻÿ�.
def convert_case(string):
    l = [x.upper() if x.islower() else x.lower() for x in string]
    return ''.join(l)
    
print(convert_case("abc Eee"))
print(convert_case("sRdE"))
print(convert_case("abcErdiu"))
print(convert_case("abc Eee"))


'''
def convert_case(string):
    s = ''
    for x in string:
        if x.islower():
            s+=x.upper()
        elif x.isupper():
            s+=x.lower()
        else:
            s+=x
    return s
'''