import mysql.connector
import pandas as pd
import sys
column_index=list(sys.argv)
x=column_index.pop(0)
user_id=column_index.pop(0)
#Reading a Csv File
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})

column_index=list(map(int,column_index))#coverted to integer
op=column_index.pop(0)#takes operater code
col_name = df.columns.tolist()#all column name

column_name = [col_name[i] for i in column_index]#selected column names
print(column_name)
#column_name=list(sys.argv[1].split(" "))# Converts the Mysql Results into pandas List
col=(":".join(column_name))
if op == 1:
	df['Mean('+col+')']=df[column_name].mean(axis=1)
elif op==2:
	df.loc['mean']=(df[column_name].mean(numeric_only=True ,axis=0))
elif op==3:
	df['Median('+col+')']=(df[column_name].median(numeric_only=True ,axis=1))
elif op==4:
	df.loc['Median']=(df[column_name].median(numeric_only=True ,axis=0))
elif op==5:
	df['Sd('+col+')']=df[column_name].std(axis=1)
elif op==6:
	df.loc['Standard Deviation']=df[column_name].std(axis=0)
elif op==7:
	df['Var('+col+')']=(df[column_name].var(numeric_only=True ,axis=1))
elif op==8:
	df.loc['Variance']=(df[column_name].var(numeric_only=True ,axis=0))
elif op==9:
	df['Min('+col+')']=df[column_name].min(axis=1)
elif op==10:
	df.loc['Minimum Value']=df[column_name].min(axis=0)
elif op==11:
	df['Max('+col+')']=df[column_name].max(axis=1)
elif op==12:
	df.loc['Maximum value']=df[column_name].max(axis=0)
elif op==13:
	df['Sum('+col+')']=df[column_name].sum(axis=1)
elif op==14:
	df.loc['Sum']=df[column_name].sum(axis=0)	

df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)
