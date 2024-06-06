import sqlite3 #This connects to sqlite

conn = sqlite3.connect('R6-Guns.db') #This connects to the 'R6-Guns.db' table

cursor = conn.cursor() #This connects to the cursur (the flashing line) in your database

def get_all_guns():
    cursor.execute('SELECT * FROM Rainbow_6_Guns;') #This tells the cursor to type/execute 'SELECT * FROM Rainbow_6_Guns;'

    all_guns = cursor.fetchall() #this gets the output of the last statment

    for gun in all_guns:
        if gun[4] == 0:
            print(f"Name: {gun[1]:<14}  Weapon Type: {gun[2]:<17} Damage: {gun[3]:<3}  Fire-rate: Single-fire  Mobility: {gun[5]:<1}  Capacity: {gun[6]:<1}")
        else:
            print(f"Name: {gun[1]:<14}  Weapon Type: {gun[2]:<17} Damage: {gun[3]:<3}  Fire-rate: {gun[4]:<4}  Mobility: {gun[5]:<1}  Capacity: {gun[6]:<1}")

def get_guns_by_high_damage():
    cursor.execute('SELECT name, weapon_type, fire_rate, damage FROM Rainbow_6_Guns ORDER BY damage DESC;')

    high_damage = cursor.fetchall()

    for gun in high_damage:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: Single-fire  Damage: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: {gun[2]:<12} Damage: {gun[3]:<5}")

def get_guns_by_low_damage():
    cursor.execute('SELECT name, weapon_type, fire_rate, damage FROM Rainbow_6_Guns ORDER BY damage')

    low_damage = cursor.fetchall()
    
    for gun in low_damage:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: Single-fire  Damage: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17} Fire rate: {gun[2]:<12} Damage: {gun[3]:<5}")

def get_guns_by_high_fire_rate():
    cursor.execute('SELECT name, weapon_type, damage, fire_rate FROM Rainbow_6_Guns ORDER BY fire_rate DESC;')

    high_fire_rate = cursor.fetchall()

    for gun in high_fire_rate:
        #print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]:<5} ")
        if gun[3] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: Single-fire")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]}")

def get_guns_by_low_fire_rate():
    cursor.execute('SELECT name, weapon_type, damage, fire_rate FROM Rainbow_6_Guns ORDER BY fire_rate')

    low_fire_rate = cursor.fetchall()

    for gun in low_fire_rate:
        if gun[3] == 0:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: Single-fire")
        else:
            print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}  Fire rate: {gun[3]}")

def get_guns_by_high_capacity():
    cursor.execute('SELECT name, weapon_type, mobility, capacity FROM Rainbow_6_Guns ORDER BY capacity DESC')

    high_capacity = cursor.fetchall()

    for gun in high_capacity:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Mobility: {gun[2]:<5}  Capacity: {gun[3]:<5}")

def get_guns_by_low_capacity():
    cursor.execute('SELECT name, weapon_type, mobility, capacity FROM Rainbow_6_Guns ORDER BY capacity')

    low_capacity = cursor.fetchall()

    for gun in low_capacity:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Mobility: {gun[2]:<5}  Capacity: {gun[3]:<5}")

def get_all_semi_auto_guns():
    cursor.execute('SELECT name, weapon_type, damage FROM Rainbow_6_Guns WHERE fire_rate = 0')

    semi_auto = cursor.fetchall()

    for gun in semi_auto:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}")


def get_all_assault_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "assault rifle"')

    assault_rifles = cursor.fetchall()

    for gun in assault_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

def get_all_light_machine_guns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "light machine gun"')

    light_machine_guns = cursor.fetchall()

    for gun in light_machine_guns:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

def get_all_marksman_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "marksman rifle"')

    marksman_rifles = cursor.fetchall()

    for gun in marksman_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

def get_all_shotguns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "shotgun"')

    shotguns = cursor.fetchall()

    for gun in shotguns:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

def get_all_sniper_rifles():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "sniper rifle"')

    sniper_rifles = cursor.fetchall()

    for gun in sniper_rifles:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

def get_all_submachine_guns():
    cursor.execute('SELECT name, damage, fire_rate, capacity FROM Rainbow_6_Guns WHERE weapon_type = "submachine gun"')

    submachine_gun = cursor.fetchall()

    for gun in submachine_gun:
        if gun[2] == 0:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: Single-fire  Capacity: {gun[3]:<5}")
        else:
            print(f"Name: {gun[0]:<16}  Damage: {gun[1]:<7} Fire rate: {gun[2]:<12} Capacity: {gun[3]:<5}")

while True:
    choice_1 = input("1 = Damage\n2 = Fire rate\n3 = Capacity\n4 = Types of weapons\n5 = All Semi-auto\n6 = All weapons\n7 = Exit\n> ")
    if choice_1 == "1":
        choice_2 = input("1 = Low to high damage\n2 = High to low damage\n> ")
        if choice_2 == "1":
            get_guns_by_low_damage()
        elif choice_2 == "2":
            get_guns_by_high_damage()
        else:
            print("unknown command. Please try again!")
    
    
    elif choice_1 == "2":
        choice_2 = input("1 = Low to high fire rate\n2 = High to low fire rate\n> ")
        if choice_2 == "1":
            get_guns_by_low_fire_rate()
        elif choice_2 == "2":
            get_guns_by_high_fire_rate()
        else:
             print("unknown command. Please try again!")
    
    
    elif choice_1 == "3":
        choice_2 = input("1 = Low to high capacity\n2 = High to low capacity\n> ")
        if choice_2 == "1":
            get_guns_by_low_capacity()
        elif choice_2 == "2":
            get_guns_by_high_capacity()
        else:
            print("unknown command. Please try again!")
    
    
    elif choice_1 == "4":
        choice_2 = input("1 = Assault rifles\n2 = Light machine guns\n3 = Marksman rifles\n4 = Shotguns\n5 = Snipers\n6 = Submachine guns\n> ")
        if choice_2 == "1":
            get_all_assault_rifles()
        elif choice_2 == "2":
            get_all_light_machine_guns()
        elif choice_2 == "3":
            get_all_marksman_rifles()
        elif choice_2 == "4":
            get_all_shotguns()
        elif choice_2 == "5":
            get_all_sniper_rifles()
        elif choice_2 == "6":
            get_all_submachine_guns()
        else:
            print("unknown command. Please try again!")
    
    
    elif choice_1 == "5":
        get_all_semi_auto_guns()   
    elif choice_1 == "6":
        get_all_guns()
    elif choice_1 == "7":
        break
    else:
        print("unknown command. Please try again!")
    