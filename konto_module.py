def karte_eingegeben(a):
    if  a == "f":
       print("erflogreich")
       return a

    else:
       print("karte ist nicht akzeptiert")

def karten_überprüfen(b):
    counter = 0
    while counter < 3:
        if b == 8431: 
            print("willkomen peter")
            break
            
            
        elif b != 8431 :
            print("passwort ist falsch bitte veruch sie es erneut")
            b = int(input())
            counter += 1
            if counter == 3:
                print("karte is gesperrt")
                break


