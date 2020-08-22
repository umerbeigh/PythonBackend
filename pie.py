
import pandas as pd
import numpy as numpy
import mysql.connector
import time
import matplotlib.pyplot as plt
import sys
user_id=sys.argv[1]
#Reading a Csv File
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})

##
style='seaborn-darkgrid'

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="mgspassing")
mycursor=mydb.cursor()

timestr=time.strftime("%Y%m%d-%H%M%S")
mycursor.execute("insert into imgpath values('','"+timestr+"','"+user_id+"')")# 1 is user id
mydb.commit()
mydb.close()

plt.style.use(style)
data=sys.argv[2]#only integer columns
label=sys.argv[3]#all columns
plt.pie(df[data],labels=df[label],startangle=15,autopct='%1.1f%%')
plt.tight_layout()
plt.axis('equal')
plt.savefig('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\images\\'+timestr+'.png')
plt.show()

