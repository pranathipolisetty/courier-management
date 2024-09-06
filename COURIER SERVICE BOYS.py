import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'bluehour', database='courier_service_system2' )
cust1=conn.cursor()

cust1.execute("insert into couriers3 values('Chennai','Mani','9123456789')")
cust1.execute("insert into couriers3 values('Chennai','Margaret','9112233445')")
cust1.execute("insert into couriers3 values('Chennai','Mani','9790345060')")
conn.commit()
