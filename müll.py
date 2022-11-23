import csv
import pandas as pd



#with open("kontodaten.txt", "r+") as file:
 #   for i in file :
  #      contant = [i.split(":")]
   #     for b in contant:
    #        print(int(b[1]) + 5)
''''
with open ('curreny_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
'''
df = pd.read_csv('curreny_data.csv')


print(df.to_string())
    

            