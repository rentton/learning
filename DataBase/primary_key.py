import sqlite3

#Create the connection
connex = sqlite3.connect("PrimaryKey")
#Create the pointer
pointer = connex.cursor()


pointer.execute('''
	CREATE TABLE STUDENTS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,	
		NAME VARCHAR(10), 
		CALIFICATION INTEGER(2))
	''')

# students = [
# 	('Juan', 8),
# 	('David', 7),
# 	('Ana', 4)
# ]

# pointer.executemany("INSERT INTO STUDENTS VALUES (NULL,?,?)",students)
# connex.commit()

pointer.execute("SELECT * FROM STUDENTS")
out = pointer.fetchall()

for i in out:
	print(i)




#Close the connection
connex.close()