import sqlite3

#Create the connection
connex= sqlite3.connect("FirstDataBase")
#Create the pointer
pointer = connex.cursor()

#Using commands
#pointer.execute(" CREATE TABLE PRODUCTS (NAME_ARTICLE VARCHAR(50), COST INTEGER, SECTION VARCHAR(20))")

#pointer.execute("INSERT INTO PRODUCTS VALUES ('BALL',20,'SPORTS')")
#connex.commit()


prods = [
    ('SHIRT',30,'CLOTHES'),
    ('TRUCK',10,'TOYS'),
    ('SHOES',60,'CLOTHES'),
    ('DOLL',15,'TOYS')
]

#! Same as pointer.executemany("INSERT INTO PRODUCTS 
#							  VALUES (?,?,?)",prods)
#Note: One ? for each value introduced
# for i in prods:
# 	pointer.execute(f"INSERT INTO PRODUCTS VALUES {i}")
# 	connex.commit()

 
pointer.execute("SELECT * FROM PRODUCTS")   
values = pointer.fetchall()

print(values)

#Close the connection
connex.close()