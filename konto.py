from timeit import repeat
import konto_module 
import keyboard


print("willkomen bei der banck austria"   "\nbitte geben sie ihre bankomant karte ein")
a = input()



def karte_eingegeben():
    if a == "f":
        print("erflogreich")

    else:
        print("karte ist nicht akzeptiert")

karte_eingegeben()
print("bitte geben sie ihr passwort ein")
b = int(input())

def karten_überprüfen(b):
    counter = 0
    for counter in range(3):
        if b == 8431: 
            print("willkomen peter")
            break
            
        elif b != 8431:
            print("passwort ist falsch bitte veruch sie es erneut")
            counter += 1

karten_überprüfen(b)
