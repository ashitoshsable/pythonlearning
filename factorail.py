def fact(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value

print(fact(int(input("Enter a number to get its factorial: "))));