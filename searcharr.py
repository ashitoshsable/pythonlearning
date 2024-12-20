from array import *

n=int(input("Enter the length of the array "))

def search(nums,value):
    for i in range(n):
        if nums[i]==value:
            return True
    return False
    # return value in nums
    
nums=array('i',[]);

for i in range(n):
    nums.append(int(input(f"Please enter the {i+1} number ")))

print(nums)

value=int(input("Enter the number you want to find in the array "))

flag=search(nums,value);

if(flag):
    print("Number found")
else:
    print("Number not found")