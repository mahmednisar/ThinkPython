from mysql import connector

mydb = connector.connect(host="localhost", user="root",password="27111996", db="naziya");

mycursor = mydb.cursor()

mycursor.execute('create table if not exists customer(name varchar(25) , mobile bigint , email varchar(50))');

sql = "INSERT INTO customer (name, mobile , email) VALUES (%s, %s , %s)"
val = [
		("a", 9549339982,"a@gmail.com"), 
		("b", 9549339982,"b@gmail.com",),
                ("c", 7465276573,"c@gmail.com")
	  ]
mycursor.executemany(sql, val)

mydb.commit()


if(mycursor.rowcount > 0):
	print(mycursor.rowcount ,  "Data inserted")
else:
	print("something went wrong")

mycursor.execute('select * from customer');
results = mycursor.fetchall();
#print(results);

for x in results:
	print(x[2])
