import math

n=15

for i in range(1,n+1):
    flag=1
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            flag=0
    if flag==1:
        print(i)

# print prime number till nth number starting from 1