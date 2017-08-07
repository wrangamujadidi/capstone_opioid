import psycopg2
import csv


with open('/Users/wrangamujadidi/Narcan_2016.csv', 'r') as f:
	reader = csv.reader(f)

	database = psycopg2.connect (database = "capstone_opioid", user="postgres", password="XXXXX", host="localhost", port="5432")

	cursor = database.cursor()

	cursor.execute("DROP TABLE narcan;")

	cursor.execute("CREATE TABLE narcan (INCIDENTN int,address1 char(100),zip varchar,latitude float,longitude float, \
		INCIDENTTYPEDISP char(10), dispatched char(50), dispositiontext char(50), age varchar, agecode char(5), \
		gendercode char (2) );")

	for row in reader:

		cursor.execute("INSERT INTO narcan VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", row)

database.commit()

cursor.close()
database.close()