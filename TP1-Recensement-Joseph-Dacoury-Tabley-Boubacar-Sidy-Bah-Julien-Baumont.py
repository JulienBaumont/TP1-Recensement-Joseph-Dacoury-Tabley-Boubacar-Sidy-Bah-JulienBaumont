import csv
#2008
table = []
with open('donnees_2008.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

table89 = []

for i in range(1, len(table)):
    if table[i][2] == '89':
        table89.append(table[i])
print("il y a ",len(table89),"communes")

j=0
hab=0
while j< len(table89):
    hab=hab+int(table89[j][9])
    j=j+1
print("En 2008,il y avais ",hab,"habitant dans l'Yonne")

#2016
table = []
with open('donnees_2016.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

table16 = []

for i in range(1, len(table)):
    if table[i][2] == '89':
        table16.append(table[i])
print("il y a ",len(table16),"communes")

j=0
hab16=0
while j< len(table16):
    hab16=hab16+int(table16[j][9])
    j=j+1
print("En 2016,il y avais ",hab16,"habitant dans l'Yonne")

#2021
table = [] 
with open('donnees_2021.csv', newline='', encoding='utf-8') as csvfile: 
    reader = csv.reader(csvfile, delimiter=';') 
    for row in reader: 
        table.append(row) 
        
table2021 = [] 
for i in range(1, len(table)): 
    if table[i][1] == '89': 
        table2021.append(table[i]) 

print("Nombre de communes en 2021 :",len(table2021)) 

h = 0 
hab21 = 0 
while h < len(table2021): 
    hab21 += int(table2021[h][5]) 
    h += 1 
print("En 2021 il y avais ",hab21,"habitants")     
#2023
table_2023 = []  

with open('donnees_2023.csv', newline='') as csvfile: 
          reader = csv.reader(csvfile, delimiter=';') 
          for row in reader: 
              table_2023.append(row) 

table23 = []  
for i in range(len(table_2023)):  
    if table_2023[i][2] == '89':  
        table23.append(table_2023[i])  
print("il y a ",len(table23),"communes") 

hab23 = 0 
for ligne in table23: 
    hab23 =hab23+ int(ligne[10])   
print("En 2023 il y avais",hab23,"habitants") 

#stats 
diff8_16=hab-hab16
diff16_21=hab16-hab21
diff21_23=hab21-hab23
moyenne=int((diff8_16+diff16_21+diff21_23)/3)
print("la moyenne d'habitants en moins chaque années est de ",moyenne,"habitants")

pourcentage= (moyenne*100/hab)
print("soit une perte de ",pourcentage,"% par année")
#courbe
dates=[2008,2016,2021,2023]
population=[hab,hab16,hab21,hab23]
from matplotlib import pyplot as plt

plt.plot(dates,population)
plt.title("Population dans l'Yonne depuis 2008 ")
plt.ylabel('Population')
plt.xlabel('Années')
plt.ylim(340000,360000)
plt.show()

