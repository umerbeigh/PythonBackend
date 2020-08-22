import mysql.connector
import pandas as pd
import sys
user_id=sys.argv[1]
#Reading a Csv File
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','na','N.A','-','none','NONE'})

col_name = df.columns.tolist()#column_names
dattypes = df.dtypes#data_types
nullcolumns = df.columns[df.isnull().any()].tolist(); #list of null columns
#Python Mysql Database Connection
con=mysql.connector.connect(host="localhost",user="root",passwd="",database="mgspassing")
cur=con.cursor()
#delete records from table
cur.execute("delete from colstructure where u_id="+user_id)
con.commit()

#insert strutre into table
for i in range(len(df.columns)):
    x = str(i)
    y='0'
    if col_name[i] in nullcolumns:
        y='1'

    dt = str(dattypes[i])
    cur.execute("insert into colstructure value('"+x+"','"+col_name[i]+"','"+dt+"','"+y+"','"+user_id+"')")
    con.commit()

cur.close()
con.close()
df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)





















