import functions
import ast
import math
from PIL import Image, ImageDraw, ImageFont

functions.popupth('fotokom.txt', "Wyjasnienie")

im = Image.open('nice.jpg')
im2 = Image.open('fotokomorka.jpg')
font_type = ImageFont.truetype('arial.ttf', 19)
draw = ImageDraw.Draw(im)
draw.text(xy=(30, 30), text='Przykładowa fotokomórka:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw2 = ImageDraw.Draw(im2)
draw2.text(xy=(20, 20), text='Uproszczony schemat fotokomórki:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
im.show()
im2.show()
font_type = ImageFont.truetype('arial.ttf', 40)
font_type1 = ImageFont.truetype('arial.ttf', 60)
im3 = Image.open('wzory.jpg')
draw = ImageDraw.Draw(im3)
draw.text(xy=(20, 50), text='OPIS MATEMATYCZNY', fill=(0, 0, 0), font=font_type1, encoding='utf-8')
draw = ImageDraw.Draw(im3)
draw.text(xy=(20, 150), text='Zjawisko fotoelektryczne zewnętrzne łatwo jest opisać następującym wzorem:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 500), text='Lewa strona równania opisuje FOTON (częstotliwość promieniowania wymnożoną przez stałą Plancka h), \nnatomiast prawa - wybity ELEKTRON (suma pracy wyjścia W oraz energii kinetycznej Ek).', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 650), text='Nasz program obliczy maksymalną energię kinetyczną jaką może uzyskać wybity elektron oraz jego \nmaksymalną prędkość dla takiej energii zgodnie ze wzorami:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 1200), text='Oraz częstotliwość graniczną wedle następującego wzoru:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
im3.show()

print("Czy chcesz wyświetlić, którąć z bibliotek?")
bibl1 = str(input())
if bibl1 == 'tak' or bibl1 == 'TAK' or bibl1 == 'Tak':
    print("Jeśli chcesz wyświetlić bibliotekę metali wpisz: 'metale', jeśli częstotliwości promieniowań, wpisz: 'fale'; Jeżeli chcesz wyświtlić obie biblioteki, wpisz 'obie'")
    ktora = str(input())
    if ktora == 'metale':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
    elif ktora == 'fale':
        functions.popupth('bibliotekafale.txt', "Biblioteka cdługości fal dla odpowiednich promieniowań:")
    elif ktora == 'obie':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
        functions.popupth('bibliotekafale.txt', "Biblioteka cdługości fal dla odpowiednich promieniowań:")

def zjawisko():
    with open("bibliotekametale.txt", "r") as data:
        bibliotekam = ast.literal_eval(data.read())

    try:
        print("Wybierz metal, dla którego chciałbyś sprawdzić czy zajdzie zjawisko; Wpisz nazwę lub skrót")
        nazwam = str(input())
        nazwam1 = nazwam.lower()
        # print(bibliotekam[nazwam1])
    except KeyError:
        print("Podanego metalu nie ma w bibliotece bądź jego nazwa została wprowadzona niepoprawnie; Spróbuj jeszcze raz:")
        nazwam = str(input())
    try:
        print("Wybierz długość fali, która ma padać na metal [nm]")
        dlugosc = float(input())
        # print(dlugosc)
    except ValueError:
        print("Wpisz wartość liczbową")
        dlugosc = float(input())

    # lewa strona rownania:
    c = 2.9979 * 10 ** 8
    f = c / (dlugosc * 10 ** (-9))
    h = float(6.63 * 10 ** (-34))
    foton = h * f
    # print(foton)

    # prawa strona rownania:
    Wev = float(bibliotekam[nazwam1]) # W w elektronowoltach
    W = Wev * 1.602 *10 ** (-19) # W w dżulach


    if foton == W:
        print("Zjawisko fotoelektryczne zachodzi; Elektron nie otrzyma dodatkowej energii kinetycznej")
    elif foton > W:
        # energia kinetyczna:
        Ek = foton - W
        me = 9.109 * 10 ** (-19)
        v = math.sqrt(2 * Ek / me)
        print("Zjawisko fotoelektryczne zachodzi; Maksymalną energią kinetyczną jaką może otrzymać elektron jest:", round(Ek, 22), "dzuli, a jego prędkość wyniesie maksymalnie", round(v, 3), "m/s.")
    else:
        print("Zjawisko elektryczne dla tego układu nie zachodzi")

zjawisko()

print("Czy chcesz spróbować ponownie?")
chcesz = str(input())
if chcesz == 'tak' or chcesz == 'TAK' or chcesz == 'Tak':
    zjawisko()
else:
    print("Dziękujemy za wypróbowanie naszego wspaniałego programu :)")

print('Czy chciał*bys wyswietlic bibliografie?')
bibl = str(input())
if bibl == 'tak' or bibl == 'TAK' or bibl =='Tak':
    functions.popupth('bibliografia.txt', "Bibliografia")