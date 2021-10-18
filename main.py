#ZAD1
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle " \
        "poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza " \
        "do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany " \
        "przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się " \
        "w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem " \
        "Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym " \
        "do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#ZAD2

imie = "Błażej"
nazwisko = "Skopnik"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print(litera_1)
print(litera_2)

liczba_liter1 = lorem.lower().count(litera_1)
liczba_liter2 = lorem.lower().count(litera_2)

print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')

#ZAD3
from datetime import datetime

ex_1 = '{:^50}'.format('Błażej wyśrodkowany na 50 polach')
ex_2 = '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))
ex_3 = '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
ex_4 = '{1} {0}'.format('one', 'two')
ex_5 = '{:>10}'.format('test')
# print(ex_1)
# print(ex_2)
# print(ex_3)
# print(ex_4)
# print(ex_5)

#Zad4

zmienna_typu_string = "Dowolny ciag tekstowy"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.title())

#Zad5
imie = "Błażej"
nazwisko = " Skopnik"
print(imie[::-1].capitalize() + " " + nazwisko[::-1].capitalize())

#Zad6

lista = list(range(1, 11))
nowa_lista = lista[5:]
lista = lista[:5]
print(lista)
print(nowa_lista)

#Zad 7

lista = lista + nowa_lista
lista.insert(0, 0)

list_copy = lista.copy()
list_copy.sort(reverse=True)
print(lista)
print(list_copy)

#Zad 8

lista_studentow = [(151621, 'Blazej Skopnik'), (123456, 'Ryszard Staruch'), (214365, 'Krzysztof Ibisz')]

print(lista_studentow)

#Zad 9 ????????????

slownik_studentów = dict(lista_studentow)
slownik_studentów['1324563'] = "25 lat,  siemanko@gmail.com, 1998, Olsztyn, Bublewicza 25"
slownik_studentów['1374563'] = "22 lata,  drugie@gmail.com, 2001, Olonsk, JakasUlica 17"
print(slownik_studentów)

#Zad 10

list_of_numbers = ['123456789', '321654987', '098678543', '123456789', '098678543', '123456679']
unique_numbers = set(list_of_numbers)

print(unique_numbers)

#Zad11
for x in range(1,11):
        print(x)

#Zad 12

for x in range(100,19,-5):
        print(x)

#Zad 13

lista_slownikow = [dict([("151621", "Błażej Skopnik"), ("321654", "Ryszard Staruch")]), dict(jeden=1, dwa=2, trzy=3)]

print(lista_slownikow)

stre = []
for x in  lista_slownikow:
        for y in x:
                stre.append(str(y))
                stre.append(str(x[y]))
                stre.append('\n')
space = ' '

print(space.join(stre))



