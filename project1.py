#!usr/bin/python3
import task_template as txt
"""
project_1.py: první projekt do Engeto Online Python Akademie
author: Ludek Fedurca
discord: fedurca#6739
"""
valid_users = {"bob": "123",
               "ann": "pass123",
               "mike": "password123",
               "liz": "pass123"}
login_req = 1
debug = 0

if (login_req):
    user = input("username:")
    pwd = input("password:")
    if user in valid_users:
        if (pwd == valid_users.get(user)):
            pass
        else:
            print("invalid password, terminating the program..")
            quit()
        print(valid_users.get(user))
    else:
        print("unregistered user, terminating the program..")
        quit()
print("-"*40)
print("Welcome to the app,", user)
print("We have 3 texts to be analyzed.")
print("-"*40)

chosen_text = input("Enter a number btw. 1 and 3 to select: ")
chosen_text = int(int(chosen_text)-1)

words_list = txt.TEXTS[chosen_text].split()

stats = {"words_count": len(words_list),
         "words_titlecase": 0,
         "words_uppercase": 0,
         "words_lowercase": 0,
         "words_numeric": 0,
         "words_sum_of_numbers": 0,
         "words_max_len": 0}

aa = 0
for aaa in words_list:
    words_list[aa] = words_list[aa].replace(",", "")
    words_list[aa] = words_list[aa].replace(".", "")
    aa += 1

for i in words_list:
    if (i.istitle()):
        stats["words_titlecase"] += 1
    if (i.isalpha() and i.isupper()):
        stats["words_uppercase"] += 1
    if (i.islower()):
        stats["words_lowercase"] += 1
    if (i.isnumeric()):
        stats["words_numeric"] += 1
        stats["words_sum_of_numbers"] += int(i)
    if (len(i) >= int(stats["words_max_len"])):
        stats["words_max_len"] = len(i)

print("There are", stats["words_count"], "words in the selected text.")
print("There are", stats["words_titlecase"], "titlecase words.")
print("There are", stats["words_uppercase"], "uppercase words.")
print("There are", stats["words_lowercase"], "lowercase words.")
print("There are", stats["words_numeric"], "numeric strings.")
print("The sum of all the numbers", stats["words_sum_of_numbers"])
print("-"*40)
print("LEN|  OCCURENCES  |NR.")
print("-"*40)

lenghts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in words_list:
    lenghts[len(i)] += 1

walk = 0

for i in range(1, int(stats["words_max_len"])+1):
    print(f'{i:>3}|{"*"*lenghts[i]:<14}|{lenghts[i]:<0}')
    walk += 1
    if (debug != 0):
        for j in words_list:
            if (len(j) == walk):
                print("SOUCASTI JE:", j)
