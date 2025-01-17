import mysql.connector as c
mydb=c.connect(host="localhost",user="root",password="1234",database="cvr")
mycursor=mydb.cursor()

#inserting a record
#mycursor.execute("insert into Customers values(6, 'Joe', 'aden', 'joe.aden@example.com', '545-7896', 'Canberra', '2024-03-15')")   

#deleting a record based on primary key
#mycursor.execute("delete from Customers where customer_id=4") 

# updating the customer details
# mycursor.execute("update Customers set first_name='mark' where last_name='aden'") 
# mycursor.execute("select * from Customers") # displaying all the customers information
# data=mycursor.fetchall()
# for customer in data:
#     print(customer)

#displaying the customers information ordered by the names in ascending order
# mycursor.execute("select * from Customers order by first_name asc")
# data=mycursor.fetchall()
# for customer in data:
#     print(customer)

#displaying the customers information where salary is between 50000 to 70000
# mycursor.execute("select * from Customers where salary between 50000 and 70000")
# data=mycursor.fetchall()
# for customer in data:
#     print(customer)

#displaying the customers information whose city is Los Angeles
mycursor.execute("select * from Customers where city='Los Angeles'")
data=mycursor.fetchall()
for customer in data:
    print(customer)

mydb.commit()
