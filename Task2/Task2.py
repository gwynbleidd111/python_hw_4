#Задача №2___________________________________________________________


def get_text():
    text = open('ice_cream.txt', 'r', encoding='utf-8')
    list = text.readlines()
    text.close()
    return list

def remove_unnecessary(list):
    list = [line.rstrip() for line in list]
    return list

def get_set_assortment(list):
    assortment = set(list[0].split(', '))
    return assortment

def get_set_in_stock(list):
    in_stock = set(list[1].split(', '))
    return in_stock

def show_not_available(assortment,in_stock):
    print("Закончилось:", *(assortment^in_stock))

a = get_text()
b = remove_unnecessary(a)
c = get_set_assortment(b)
d = get_set_in_stock(b)
show_not_available(c,d)
