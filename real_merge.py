import pandas as pd
import os

l=os.listdir()


data=pd.read_csv(l[0],sep='|')



for i in range(1,len(l)):
	if(l[i]!="main.csv"):
		temp=pd.read_csv(l[i],sep='|',error_bad_lines=False)
		data=pd.concat([data,temp])
		data=data.reset_index(drop=True)


data.to_csv("real_meta.csv")



