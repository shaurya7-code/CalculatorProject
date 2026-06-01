import pandas as pd
a=[x for x in range(4)]
b=[x for x in  "ABCD"]
c=pd.Series(data=a,index=b)
print(c)
