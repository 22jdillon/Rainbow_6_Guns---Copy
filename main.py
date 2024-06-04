import sqlite3 #This connects to sqlite

conn = sqlite3.connect('R6-Guns.db') #This connects to the 'R6-Guns.db' table

cursor = conn.cursor() #This connects to the cursur (the flashing line) in your database

cursor.execute('SELECT * FROM Rainbow_6_Guns;') #This tells the cursor to type/execute 'SELECT * FROM Rainbow_6_Guns;'

guns = cursor.fetchall() #this gets the output of the last statment

print(guns) #this prints the output of the execution
for gun in guns:
    print(f"Name: {gun[1]} Weapon Type: {gun[2]} Damage: {gun[3]}, Fire rate: {gun[4]}, Mobility: {gun[5]} and Capacity: {gun[6]}")