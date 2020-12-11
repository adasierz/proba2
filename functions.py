import ctypes
import codecs
import ast

def popupth(nazwa, tytul):
    # tutaj jest mala funkcja ktora otwiera nasze okienko z wyjasnieniem Z POLSKIMI ZNAKAMI :))))))
    popup = ''
    with codecs.open(nazwa, encoding='utf-8') as f:
        for line in f:
            popup = popup + line
    ctypes.windll.user32.MessageBoxW(0, popup, tytul, 1)
def openandread(plik, nazwam):
    file2 = codecs.open(plik, encoding='utf-8')
    f2 = file2.readlines()
    theone = ''
    d = {}
    #for line in f2: 
        #for word in line.split(): 
            #if word == nazwam:
               #theone = word
               #print(word)
    contents = file2.read()
    dictionary = ast.literal_eval(contents)
    file2.close()
    print(type(dictionary))
    print(dictionary)

    
        