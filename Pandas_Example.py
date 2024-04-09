import numpy as np
import pandas as pd
l1=["500124909","Sai","Uppalapati","DSA","B51"]
l2=["500124929","Shubham","Negi","Python","B51"]
l3=["500124521","Harshit","Agarwal","COA","B51"]
df=pd.DataFrame(data=np.array([l1,l2,l3]))
print(df)
a2=np.array([l1,l2,l3])
print(a2)
a2[2]="Seshu"
print(a2)
