import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'bluehour', database='courier_service_system2' )
cust1=conn.cursor()
cust1.execute('create table couriers2(Weight_in_kgs varchar(789),Cost_in_rupees varchar(789));')
