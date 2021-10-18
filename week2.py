#Zad 1

def fun1(a_list, b_list):
    resutl = [];
    for even in a_list:
        if a_list.index(even) % 2 == 0:
            resutl.append(a_list.index(even))
    for odd in b_list:
        if b_list.index(odd) % 2 != 0:
            resutl.append(b_list.index(odd))
    return resutl


list_a = [5, 4, 3, 2, 1, 0, 'dsa']
list_b = [1, 5, 32, 543, 76, 2, 3]

print(fun1(list_a, list_b))

#Zad 2


def fun2(data_text):
    length = len(data_text)
    letters = [i for i in data_text]
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    result = dict([('length', length), ('letters', letters),
                   ('big_letters', big_letters), ('small_letters', small_letters)])
    return result


print(fun2('Ojacie ale fajny Przedmiot'))

#Zad 3


def fun3(text, letter):
    return text.replace(letter, '')


print(fun3('I am awesome', 'a'))
#Zad 4


def fun4(celsius_degree, temperature_type='Fahrenheit'):
    if temperature_type == 'Fahrenheit':
        return (celsius_degree * 9)/5 + 32
    elif temperature_type == 'Rankine':
        return (celsius_degree * 1.8) + 491.67
    elif temperature_type == 'Kelwin':
        return celsius_degree + 273.15
    else:
        return 'Temperature type was wrong, try again with: Fahrenheit, Kelwin or Rankine'


print(fun4(10, "Kelwin"))

#Zad 5

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calk = Calculator(3,6)

print(calk.divide(4,7))

#Zad 6

class ScienceCalculator(Calculator):
    def power(self, a, b):
        return a ** b

sciCalc = ScienceCalculator(4,6)
print(sciCalc.power(2, 10))

#Zad 7


def back_to_front(text):
    return text[::-1]


print(back_to_front('Siemanko byczku, jak się masz'))



#Zad 9

import file_manager


print(file_manager.FileManager("plik.txt").read_file())

file_manager.FileManager("plik.txt").update_file("\nNapotkala mysliweczka bardzo szwarnego")

print(file_manager.FileManager("plik.txt").read_file())
