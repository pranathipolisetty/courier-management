import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'bluehour', database='courier_service_system2' )
cust1=conn.cursor()
cust1.execute('create table couriers(customer_name varchar(99) ,customer_mobile_number varchar(789),customer_address text(789),receiver_name varchar(99) ,receiver_mobile_number varchar(789),receiver_address text(789))')
CUST=cust1.fetchall()
for s in CUST:
     print(s)
    
          

