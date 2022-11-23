"das ist mein main klasse was ich imoprtet habe ist os für die files zu lesen , timeit für das ich ein loop machen wenn ich es f



from os import read
from timeit import repeat
import konto_module as rasa
import keyboard
import time

einzahlen = "1: einzahlen"
auszahlen = "2: auszahlen"
kontostand = "3: kontostand"
c = [einzahlen , auszahlen, kontostand ]
file = open("C:\\USERS\expla\konto\kontodaten.txt")
print(file)

print(file.read())
print("willkomen bei der banck austria"   "\nbitte geben sie ihre bankomant karte ein")
global a 
a = input()

rasa.karte_eingegeben(a)
print("bitte geben sie ihr passwort ein")
b = int(input())
            
rasa.karten_überprüfen(b)

print("bitte wählen sie eine option aus")
time.sleep(1.5)


def sort_list(c):
    for liste in c:
        print(liste)
        print("")
        

sort_list(c)
z = input(int())

#def choose_option(d):
 #   if z == 1:
 #       


"""""
def einzahlen():
    print("wählen sie das konto aus")
    print(file)
    konto = input(int())
    if konto == 1:
"""




