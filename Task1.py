#Задача №1___________________________________________________________

def get_number():
    number = int(input("Введите число: "))
    return number

def get_multipliers(number):
    i = 2
    multipliers = []
    while i * i <= number:
        while number % i == 0:
            multipliers.append(i)
            number = number // i
        i = i + 1
    if number > 1:
        multipliers.append(number)
    return multipliers

def transformation(list):
    new_list = ', '.join([str(x) for x in list])
    return new_list

def write(list):
    data = open("text.txt", "w")
    data.writelines(list)
    data.close()

a = get_number()
b = get_multipliers(a)
c = transformation(b)
write(c)
