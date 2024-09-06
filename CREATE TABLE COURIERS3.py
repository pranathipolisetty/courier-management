import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'bluehour', database='courier_service_system2' )
cust1=conn.cursor()
cust1.execute('create table couriers3(city varchar(99),courier_boys varchar(99),courier_service_boys_mob_number varchar(99));')
