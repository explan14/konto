import time
import csv

file = open('C:\\USERS\expla\konto\kontodaten.txt', 'w+')
print(file)





def currency_calculator(file):
    print("bitte geben sie ihre gewünschte zahlungsmittel ein ")
    time.sleep(1.5)
    print("1: Geld \n2: Crypto")
    time.sleep(1.1)
    wählen = input("Bitte wählen sie :" )
    if wählen == "geld":
        return

    elif wählen == "crypto":
        return

    return


def paper_currency(file):
    print("Bitte wählen sie ihr konto aus ")
    time.sleep(1.0)
    print("Girokonto:  \n Sparkonto:  ")
    konto1 = input("Bitte wählen:")
    def file_processer(eingabe3):
        with open("kontodaten.txt", "r") as file:
            content = eingabe3
            listes = [line.strip(":") for line in file]

        for line in listes:
            print(line.strip())
            

    if konto1 == "Girokonto":
        print("Bitte Wählen sie ihre Gewünschte Währung ")
        time.sleep(1.0)
        #currency_list = ["euro", "doller", "chf","rubel","pfund"]
        print("Euro" , "Doller" , "CHF" , "rubel" ,  "Pfund")
        eingabe1 = input("bitte eingeben")
        
        if eingabe1 == "euro":
            betrag = input("")
            return
        elif eingabe1 == "dollar":
            return
        elif eingabe1 == "chf":
            return
        elif eingabe1 == "rubel":
            return
        elif eingabe1 == "pfund":
            return







''''
print("bitte geben sie ihre gewünschte zahlungsmittel ein ")
time.sleep(1.5)
print("1: Geld \n2: Crypto")
time.sleep(1.1)
wählen = input("Bitte wählen sie :" )
''''
