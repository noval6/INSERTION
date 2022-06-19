import pandas as pd
import csv
df=pd.read_csv(r'D:/code/Google Scholar - Top English Publications.csv')
data = pd.DataFrame(df, columns= ['Publication' , 'h-5median'])
print(data)

def insert_sort(arr):
    n = len(arr)
    for i in range(len(arr)-1):
 
        key = arr[i][n]
 
        n = i-1
        if n >=0 and key < arr[n]:
                arr[n+1] = arr[n]
                n -= 1
        arr[n+1] = key

print("Insert Sort")