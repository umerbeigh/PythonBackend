import pandas as pd
import sys
user_id=sys.argv[1]
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','na','N.A','-','none','NONE'})
column_index=int(sys.argv[2])
column_name=df.columns[column_index]#column name from column index
mean_value=df[column_name].mean()#calculate mean for column
df[column_name]=df[column_name].fillna(mean_value)#fill nan or emty cell with that mean 
df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)
