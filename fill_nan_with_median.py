import pandas as pd
import sys
user_id=sys.argv[1]
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})
column_index=int(sys.argv[2])
column_name=df.columns[column_index]#column name from column index
#Fill a Particular Column NaN Values with its median
median_value=df[column_name].median()
df[column_name]=df[column_name].fillna(median_value)
df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)

