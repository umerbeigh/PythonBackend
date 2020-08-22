import mysql.connector
import pandas as pd
import sys
#Reading a Csv File
user_id=sys.argv[1]
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})
#Python Mysql Database Connection
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="mgspassing")
mycursor=mydb.cursor()

#Fetching teh result from database & renaming  all columns


mycursor.execute('select col_name,newcolname from colstructure,rename_col where colstructure.u_id='+user_id+' and col_index=c_index')
col_names=mycursor.fetchall()
mycursor.execute("delete from rename_col where u_id="+user_id)
mydb.commit()
mycursor.close()
mydb.close()
res ={sub[0]:sub[1] for sub in col_names}

df.rename(columns=res,inplace=True)

df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)
