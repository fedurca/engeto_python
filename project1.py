#/usr/bin/python3

import textin as txt

"""
project_1.py: první projekt do Engeto Online Python Akademie
author: Ludek Fedurca
email: fedurca@odbornaskola.cz
discord: fedurca#6739

bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123
"""

valid_users = { "bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123" }
login_req=0
debug=0

if (login_req):
    user = input("login:")
    #print(user)
    pwd = input("password:")
    #print(user)
    if user in valid_users:
        print("user OK")
        #print(user, valid_users[user])
        if (pwd == valid_users.get(user)):
            print("password OK")
        else: 
            print("invalid password")
        print(valid_users.get(user))
    else:
        print("user not OK")

    #vypsat prvni text
    #print(txt.TEXTS[0])

chosen_text = input("Enter a number btw. 1 and 3 to select: 1")
chosen_text = int(chosen_text)-1

#sentence = "This is a test"
words_list = txt.TEXTS[chosen_text].split()
#print(len(words_list))

stats={ "words_count":len(words_list),
        "words_titlecase":0, 
        "words_uppercase":0,
        "words_lowercase":0,
        "words_numeric":0,
        "words_sum_of_numbers":0,
        "words_max_len":0
       }

aa=0
for aaa in words_list:
    words_list[aa] = words_list[aa].replace(",", "")
    words_list[aa] = words_list[aa].replace(".", "")
    aa+=1
    #print(aa)
    

for i in words_list:
    #print(i)
    if (i.istitle()):
        stats["words_titlecase"]+=1
        #print("INCREMENTING")
    if (i.isalpha() and i.isupper()):
        stats["words_uppercase"]+=1
        #print("UPPER:",i)
    if (i.islower()):
        stats["words_lowercase"]+=1
    if (i.isnumeric()):
        stats["words_numeric"]+=1
        #print("RECOGNIZED NUMBER IS:",i)
        stats["words_sum_of_numbers"]+=int(i)
    if (len(i) >= int(stats["words_max_len"]) ):
        #print("MAXLEN",i)
        stats["words_max_len"]=len(i)

print("There are", stats["words_count"],"words in the selected text.")
print("There are", stats["words_titlecase"],"titlecase words.")
print("There are", stats["words_uppercase"],"uppercase words.")
print("There are", stats["words_lowercase"],"lowercase words.")
print("There are", stats["words_numeric"],"numeric strings.")
print("The sum of all the numbers", stats["words_sum_of_numbers"])
print("-"*40)
print("LEN|  OCCURENCES  |NR.")
print("-"*40)

lenghts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  

for i in words_list:
    #if (len(i) == 1):
    lenghts[len(i)]+=1

walk=0

for i in range(1,int(stats["words_max_len"])+1):
    print(f'{i:>3}|{"*"*lenghts[i]:<14}|{lenghts[i]:<0}')
    #print(i,"|","X"*lenghts[i],"|",lenghts[i])
    walk+=1
    
    if (debug!=0):
        for j in words_list:
            if (len(j) == walk):
                print("SOUCASTI JE:",j)

#print(lenghts)


