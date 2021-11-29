import sqlite3

#Create the connection
connex= sqlite3.connect("Unique")
#Create the pointer
pointer = connex.cursor()

# pointer.execute('''
#         CREATE TABLE ALUMNS (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#         NAME VARCHAR(10), 
#         DNI INTEGER(8) UNIQUE )
#     ''')

# alumns = [
#     ("Pepe",25620789),
#     ("Susan", 29087654)
# ]

# pointer.executemany('''INSERT INTO ALUMNS 
#     VALUES (NULL,?,?)''',alumns)
# connex.commit()
 
pointer.execute("SELECT * FROM ALUMNS WHERE DNI = 29087654")   
values = pointer.fetchall()
print(values)


pointer.execute('''INSERT INTO ALUMNS 
     VALUES (NULL,"David",34567890) ''')


pointer.execute('''UPDATE ALUMNS SET NAME="Dan"
    WHERE DNI = 25620789 ''')


pointer.execute("SELECT * FROM ALUMNS")   
values = pointer.fetchall()
print(values)

pointer.execute("DELETE FROM ALUMNS WHERE DNI=25620789")

pointer.execute("SELECT * FROM ALUMNS")   
values = pointer.fetchall()
print(values)

#Close the connection
connex.close()