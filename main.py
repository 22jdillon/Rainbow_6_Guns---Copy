import sqlite3 #This connects to sqlite

import os #This imports the thing where it clears the terminal when its used 

conn = sqlite3.connect('R6-Guns.db') #This connects to the 'R6-Guns.db' table

cursor = conn.cursor() #This connects to the cursur (the flashing line) in your database    

def siege_guns():
    print(R"""
 ______     __     ______     ______     ______        ______     __  __     __   __     ______    
/\  ___\   /\ \   /\  ___\   /\  ___\   /\  ___\      /\  ___\   /\ \/\ \   /\ "-.\ \   /\  ___\   
\ \___  \  \ \ \  \ \  __\   \ \ \__ \  \ \  __\      \ \ \__ \  \ \ \_\ \  \ \ \-.  \  \ \___  \  
 \/\_____\  \ \_\  \ \_____\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_\\"\_\  \/\_____\ 
  \/_____/   \/_/   \/_____/   \/_____/   \/_____/      \/_____/   \/_____/   \/_/ \/_/   \/_____/ 
                                                                                                   """)
#I defined this becuase it makes the code neat when i call on it

def continue_():
    input("Click any button to continue\n> ")
#I defined this becuase it makes the code neat when i call on it, it just a thing where you press enter and then it conrtiniose to the next line

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#I defined this becuase it makes the code neat when i call on it, it clears the terminal so the code look nice and clean

def get_all_guns():
    cursor.execute('SELECT * FROM Rainbow_6_Guns;') #This tells the cursor to type/execute 'SELECT * FROM Rainbow_6_Guns;'

    all_guns = cursor.fetchall() #this gets the output of the last statment

    for gun in all_guns: # this loops as many times there is lists in all_guns
        if gun[4] == 0: #this ditects if gun[4]/fire rate is 0, if it is it print "single-fire" insted of printing 0 so it makes it more clear to the user
            print(f"Name: {gun[1]:<14}  Weapon Type: {gun[2]:<17} Damage: {gun[3]:<3}  Fire-rate: Single-fire      Mobility: {gun[5]:<1}  Capacity: {gun[6]:<1}")
        else:   #if the fire rate is more not zero it prints this code
            print(f"Name: {gun[1]:<14}  Weapon Type: {gun[2]:<17} Damage: {gun[3]:<3}  Fire-rate: {gun[4]:<15}  Mobility: {gun[5]:<1}  Capacity: {gun[6]:<1}")

def get_guns_by_high_damage():
    cursor.execute('SELECT name, weapon_type, fire_rate, damage FROM Rainbow_6_Guns ORDER BY damage DESC;')

    high_damage = cursor.fetchall()

    for gun in high_damage:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: Single-fire  Damage: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: {gun[2]:<12} Damage: {gun[3]:<5}")
#this section sorts the damage of all the guns in r6 and sorts it form high to low

def get_guns_by_low_damage():
    cursor.execute('SELECT name, weapon_type, fire_rate, damage FROM Rainbow_6_Guns ORDER BY damage')

    low_damage = cursor.fetchall()
    
    for gun in low_damage:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: Single-fire  Damage: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: {gun[2]:<12} Damage: {gun[3]:<5}")
#this section sorts the damage of all the guns in r6 and sorts it form low to high

def get_guns_by_high_fire_rate():
    cursor.execute('SELECT name, weapon_type, damage, fire_rate FROM Rainbow_6_Guns ORDER BY fire_rate DESC;')

    high_fire_rate = cursor.fetchall()

    for gun in high_fire_rate:
        #print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]:<5} ")
        if gun[3] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: Single-fire")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]}")
#this section sorts the fire rate of all the guns in r6 and sorts it form high to low

def get_guns_by_low_fire_rate():
    cursor.execute('SELECT name, weapon_type, damage, fire_rate FROM Rainbow_6_Guns ORDER BY fire_rate')

    low_fire_rate = cursor.fetchall()

    for gun in low_fire_rate:
        if gun[3] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: Single-fire")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]}")
#this section sorts the fire rate of all the guns in r6 and sorts it form low to high

def get_guns_by_high_capacity():
    cursor.execute('SELECT name, weapon_type, mobility, capacity FROM Rainbow_6_Guns ORDER BY capacity DESC')

    high_capacity = cursor.fetchall()

    for gun in high_capacity:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Mobility: {gun[2]:<5}  Capacity: {gun[3]:<5}")
#this section sorts the capacity of all the guns in r6 and sorts it form high to low

def get_guns_by_low_capacity():
    cursor.execute('SELECT name, weapon_type, mobility, capacity FROM Rainbow_6_Guns ORDER BY capacity')

    low_capacity = cursor.fetchall()

    for gun in low_capacity:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Mobility: {gun[2]:<5}  Capacity: {gun[3]:<5}")
#this section sorts the capacity of all the guns in r6 and sorts it form low to high

def get_all_semi_auto_guns():
    cursor.execute('SELECT name, weapon_type, damage FROM Rainbow_6_Guns WHERE fire_rate = 0')

    semi_auto = cursor.fetchall()

    for gun in semi_auto:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}")
#this section sorts all the semi automatic guns 

def get_all_assault_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "assault rifle"')

    assault_rifles = cursor.fetchall()

    for gun in assault_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sorts all the assault 

def get_all_light_machine_guns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "light machine gun"')

    light_machine_guns = cursor.fetchall()

    for gun in light_machine_guns:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sorts all the LMGs

def get_all_marksman_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "marksman rifle"')

    marksman_rifles = cursor.fetchall()

    for gun in marksman_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sorts all the marksman rifles

def get_all_shotguns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "shotgun"')

    shotguns = cursor.fetchall()

    for gun in shotguns:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sorts all the shotguns

def get_all_sniper_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "sniper rifle"')

    sniper_rifles = cursor.fetchall()

    for gun in sniper_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sortts all the sniper rilfes 

def get_all_submachine_guns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "submachine gun"')

    submachine_gun = cursor.fetchall()

    for gun in submachine_gun:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")
#this section sorts all the submachine guns

while True: #this creates an loop that will repete forever untill you "break" it or if its overrun by another loop.
    siege_guns()
    #this calls on the title
 
    choice_1 = input("1 = Damage\n2 = Fire rate\n3 = Capacity\n4 = Types of weapons\n5 = All Semi-auto\n6 = All weapons\n7 = Exit\n> ")
    #this asks you which choices you have
    clear()
    #this clears all the text
    if choice_1 == "1": #this detects if the user inputed 1 for choice_1
        while True: #this creates an loop forever loop inside a forever loop that will repete forever untill you "break" it.
            choice_2 = input("1 = Low to high damage\n2 = High to low damage\n> ")
            clear()
            if choice_2 == "1":
                get_guns_by_low_damage()
                continue_()
                clear()
                break # this breaks the loop which makes it go back to the 1st forever loop
            elif choice_2 == "2":
                get_guns_by_high_damage()
                continue_()
                clear()
                break
            else:
                print("Unknown command. Please try again!\nPlease enter the corresponding number:\n") # if you entered the an unxseptable input it will tell you to try again until its right.
    
    elif choice_1 == "2":
        while True:
            choice_2 = input("1 = Low to high fire rate\n2 = High to low fire rate\n> ")
            clear()
            if choice_2 == "1":
                get_guns_by_low_fire_rate()
                continue_()
                clear()
                break
            elif choice_2 == "2":
                get_guns_by_high_fire_rate()
                continue_()
                clear()
                break
            else:
                print("Unknown command. Please try again!\nPlease enter the corresponding number:\n")
    
    elif choice_1 == "3":
        while True:
            choice_2 = input("1 = Low to high capacity\n2 = High to low capacity\n> ")
            clear()
            if choice_2 == "1":
                get_guns_by_low_capacity()
                continue_()
                clear()
                break
            elif choice_2 == "2":
                get_guns_by_high_capacity()
                continue_()
                clear()
                break
            else:
                print("Unknown command. Please try again!\nPlease enter the corresponding number:\n")
    
    elif choice_1 == "4":
        while True:
            choice_2 = input("1 = Assault rifles\n2 = Light machine guns\n3 = Marksman rifles\n4 = Shotguns\n5 = Snipers\n6 = Submachine guns\n> ")
            clear()
            if choice_2 == "1":
                get_all_assault_rifles()
                continue_()
                clear()
                break
            elif choice_2 == "2":
                get_all_light_machine_guns()
                continue_()
                clear()
                break
            elif choice_2 == "3":
                get_all_marksman_rifles()
                continue_()
                clear()
                break
            elif choice_2 == "4":
                get_all_shotguns()
                continue_()
                clear()
                break
            elif choice_2 == "5":
                get_all_sniper_rifles()
                continue_()
                clear()
                break
            elif choice_2 == "6":
                get_all_submachine_guns()
                continue_()
                break
            else:
                print("Unknown command. Please try again!\nPlease enter the corresponding number:\n")
    
    elif choice_1 == "5":
        get_all_semi_auto_guns()   
        continue_()
        clear()
    elif choice_1 == "6":
        get_all_guns()
        continue_()
        clear()
    elif choice_1 == "7":
        print(R"""
______                                                     _          _ 
| ___ \                                                   | |        | |
| |_/ / __ ___   __ _ _ __ __ _ _ __ ___     ___ _ __   __| | ___  __| |
|  __/ '__/ _ \ / _` | '__/ _` | '_ ` _ \   / _ \ '_ \ / _` |/ _ \/ _` |
| |  | | | (_) | (_| | | | (_| | | | | | | |  __/ | | | (_| |  __/ (_| |
\_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_|  \___|_| |_|\__,_|\___|\__,_|
                __/ |                                                  
                |___/                                                   """)
        break # this breaks the main loop and end the whole program
    else:
        print("Unknown command. Please try again!\nPlease enter the corresponding number:\n")
#this is the menu 