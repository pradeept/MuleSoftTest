import sqlite3

conn = sqlite3.connect('Movies.db')
cur = conn.cursor()

def creating():

	#For creating Table
	cur.execute("""CREATE TABLE Movies(
				movie_name text,
				actor text,
				actress  text,
				year_of_release  integer,
				director_name text
				)
				""")
	print("Table Creation Successful!")
	conn.commit()
	conn.close()

def inserting():
	values = [
				('Spider-Man No-Way-Home','Tom Holland','Zendaya',2021,'Jon Watts'),
				('The Fault in Our Stars','Ansel Elgort','Shailene Woodley',2014,'Josh Boone'),
				('Joker','Joaquin Phoenix','Zazie Beetz',2019,'Todd Phillips'),
				('Black Panther','Chadwick','Lupita',2018,'Ryan Coogler'),
				
			]	
	#Inserting Values into Movies
	cur.executemany("INSERT INTO Movies VALUES(?,?,?,?,?)", values)

	print("Values Inserted Successfully!")
	conn.commit()
	conn.close()


def querying():
	#querying the data using SELECT
	cur.execute("SELECT * FROM Movies")

	print(cur.fetchall())

	#Displaying movie name of particular Actor
	cur.execute("SELECT * FROM Movies WHERE actor='Tom Holland'")
	print(cur.fetchall())


	conn.commit()
	conn.close()

creating()
inserting()
querying()
