import sqlite3 #This connects to sqlite

conn = sqlite3.connect('R6-Guns.db') #This connects to the 'R6-Guns.db' table

cursor = conn.cursor() #This connects to the cursur (the flashing line) in your database

def get_all_guns():
    cursor.execute('SELECT * FROM Rainbow_6_Guns;') #This tells the cursor to type/execute 'SELECT * FROM Rainbow_6_Guns;'

    all_guns = cursor.fetchall() #this gets the output of the last statment

    for gun in all_guns:
        print(f"Name: {gun[1]:<14} Weapon Type: {gun[2]:<17} Damage: {gun[3]:<3} Fire rate: {gun[4]:<4} Mobility: {gun[5]:<1} Capacity: {gun[6]:<1}")

def get_guns_by_damage():

    cursor.execute('SELECT name, weapon_type, damage FROM Rainbow_6_Guns ORDER BY damage DESC;')

    high_damage = cursor.fetchall()

    for gun in high_damage:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}")

def get_guns_by_fire_rate():

    cursor.execute('SELECT name, weapon_type, fire_rate FROM Rainbow_6_Guns WHERE fire_rate > 0 ORDER BY fire_rate DESC;')

    high_fire_rate = cursor.fetchall()

    for gun in high_fire_rate:
        print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Fire rate: {gun[2]:<5}")

while True:
    choice = input("\n1 = Get all\n2 = Get damage \n3 = Get fire rate\n4 = Exit\n> ")
    if choice == "1":
        get_all_guns()
    elif choice == "2":
        get_guns_by_damage()
    elif choice == "3":
        get_guns_by_fire_rate()
    elif choice == "4" :
        break
    else:
        print("\nInvalid input!")


