import pandas as pd
import sys

#Reading a Csv File
user_id=sys.argv[1]
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})

#Droping Columns containing a Null Value
df.dropna(axis=1,how='any',inplace=True )
#Writing back to the Csv file
df.to_csv('C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\'+user_id+'\\temp.csv',encoding='utf-8',index=False)
