#/usr/bin/python3
import random
"""
project2.py: druhý projekt do Engeto Online Python Akademie (tic tac toe)
author: Ludek Fedurca
discord: fedurca#6739
"""

herni_pole=[" "," "," ",
            " "," "," ",
            " "," "," "]
pocet_sloupcu = 3

def vykresli_hru():
    i=1
    for kamen in herni_pole:
        print("",end ="|")
        print(herni_pole[i-1],end ="")
        #print("|",herni_pole[i-1])
        if (i%pocet_sloupcu == 0): print("|")
        i+=1
    print("")
        
#vykresli_hru()
#herni_pole[1] = "X"
vykresli_hru()
"""
konec_hry=False

while (konec_hry == False):
    herni_pole=[" "," "," ",
            " "," "," ",
            " "," "," "]
"""
nemame_viteze = True
while (nemame_viteze):
    tah = input("zadej svůj tah (1-9):")
    if (herni_pole[int(tah)-1] == " " ): 
        herni_pole[int(tah)-1] = "0"
    else:
        print("neplatný tah - pozice obsazena")
        continue
    #print("pruchod cyklem")
    vykresli_hru()

    volne_pole = True
    while (volne_pole):
        tah = random.randint(1,9)
        if (herni_pole[int(tah)-1] == " " ): 
            herni_pole[int(tah)-1] = "X"
            volne_pole=False
#        else:
#            pass
    print("táhne počítač..")
    vykresli_hru()
    
    if (herni_pole[0] != " " and herni_pole[0] == herni_pole[1] and herni_pole[0] == herni_pole[2]):
        print("Vítěz je:",herni_pole[0])
        nemame_viteze = False
        break
    elif (herni_pole[0+3] != " " and herni_pole[0+3] == herni_pole[1+3] and herni_pole[0+3] == herni_pole[2+3]):
        print("Vítěz je:",herni_pole[0+3])
        nemame_viteze = False
        break
    elif (herni_pole[0+3+3] != " " and herni_pole[0+3+3] == herni_pole[1+3+3] and herni_pole[0+3+3] == herni_pole[2+3+3]):
        print("Vítěz je:",herni_pole[0+3+3])
        nemame_viteze = False
        break
    ##check vertical win
    elif (herni_pole[0] != " " and herni_pole[0] == herni_pole[3] and herni_pole[3] == herni_pole[6]):
        print("Vítěz je:",herni_pole[0])
        nemame_viteze = False
        break
    elif (herni_pole[0+1] != " " and herni_pole[0+1] == herni_pole[3+1] and herni_pole[3+1] == herni_pole[6+1]):
        print("Vítěz je:",herni_pole[0+1])
        nemame_viteze = False
        break
    elif (herni_pole[0+2] != " " and herni_pole[0+2] == herni_pole[3+2] and herni_pole[3+2] == herni_pole[6+2]):
        print("Vítěz je:",herni_pole[0+2])
        nemame_viteze = False
        break
    ##check diagonal win
    elif (herni_pole[0] != " " and herni_pole[0] == herni_pole[4] and herni_pole[4] == herni_pole[8]):
        print("Vítěz je:",herni_pole[0])
        nemame_viteze = False
        break
    elif (herni_pole[2] != " " and herni_pole[2] == herni_pole[4] and herni_pole[4] == herni_pole[6]):
        print("Vítěz je:",herni_pole[2])
        nemame_viteze = False
        break
    else:
        print("Vítěz zatim neni")
        nemame_viteze = True
       
    
print("konec hry")
