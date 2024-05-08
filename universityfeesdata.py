import numpy as np
import pandas as pd
df=pd.read_csv("tuition_cost.csv")
r=input()
lista=r.split(" ")
if lista[0]=="P":
 print("%.2f"%np.percentile(df[lista[2]],q=int(lista[1])))
elif lista[0]=="M":
  print("%.2f"%df[lista[1]].mean(),"%.2f"%df[lista[1]].std())
elif lista[0]=="A":
  print("%.2f"%(df[lista[1]].max()-df[lista[1]].min()))
elif lista[0]=="Q":
  print(len(df.query(lista[3] + ">=" + lista[1] + "and " + lista[3] + "<=" + lista[2]))) 
else:
  print("Deu ruim")