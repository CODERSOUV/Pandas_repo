import pandas as pd

# df=pd.DataFrame({"jaipur": [1,2,3,4,5], "delhi": [6,7,8,9,10], "mumbai": [11,12,13,14,15], "kolkata": [16,17,18,19,20]})
df=pd.DataFrame(data=[[1,2,3,4],[3,4,5,6]],index=["x","y"],columns=['a','b','c','d'])
print(df)