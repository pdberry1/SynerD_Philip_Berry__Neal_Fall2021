import mysql.connector
from DonorDB import donor, company, donation

hostname = 'localhost'
username = 'tzxlqfzc'
password = 'EJPHY6LoqMQIb8NpA0LBI0frA_duDb8k'
database = 'tzxlqfzc'

print("Content-type: text/html\n\n")

mydb = mysql.connector.connect (host=hostname, user=username, pw=password, db= database)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM donor")
insert into donor (donor_first_name, donor_last_name) values ('Tiger', 'Woods')
delete * from donor where donor_first_name = "test"
update donor () where donor_first_name = 'test'
myresult = mycursor.fetchall()

for x in myresult:
	print(x+"<br><br>")
	
myConnection.close()