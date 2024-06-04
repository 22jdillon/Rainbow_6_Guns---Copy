import sqlite3 #This connects to sqlite

conn = sqlite3.connect('R6-Guns.db') #This connects to the 'R6-Guns.db' table

cursor = conn.cursor() #This connects to the cursur (the flashing line) in your database

cursor.execute('SELECT * FROM Rainbow_6_Guns;') #This tells the cursor to type/execute 'SELECT * FROM Rainbow_6_Guns;'

guns = cursor.fetchall() #this gets the output of the last statment

for gun in guns:
    print(f"Name: {gun[1]:<16}  Weapon Type: {gun[2]:<20}  Damage: {gun[3]:<5}  Fire rate: {gun[4]:<6}  Mobility: {gun[5]:<5}  Capacity: {gun[6]:<7}")

cursor.execute('SELECT name, weapon_type, damage FROM Rainbow_6_Guns ORDER BY damage DESC;')

guns = cursor.fetchall()

for gun in guns:
    print(f"Name: {gun[0]:<16}  Weapon Type: {gun[1]:<17}  Damage: {gun[2]:<5}")