from numpy import *

num1=array([1,2,3,4,5,6,7,8,9])
num2=array([2,3,4,5,6,7,8,9,10])

num3=num1.view()
print(num3,id(num3))

num=num1+num2
print(num)
