import pandas as pd
import sys
#Reading a Csv File
user_id=sys.argv[1]
df=pd.read_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",na_values={'n.a','N.A','-','none','NONE'})
# Droping All rows With NaN value in any cell
df.dropna(inplace=True)


#Writing back to the Csv file
df.to_csv("C:\\xampp\\tomcat\\webapps\\dataclean\\Users\\"+user_id+"\\temp.csv",encoding='utf-8',index=False)
