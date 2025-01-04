def fibonacci(n):
    if n<1:
        print("Give a positive integer!")
    elif n==1:
        print(0);
    else:
        pprev=0
        prev=1
        print(pprev)
        print(prev)
        for i in range(2,n):
            temp=pprev+prev
            print(temp)
            pprev=prev
            prev=temp

fibonacci(int(input("Enter a positive number: ")))