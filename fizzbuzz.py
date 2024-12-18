n=100

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


# if, elif and else
# Q. if number is divisble by 3 print "Fizz", if number is divisible by 5 print "Buzz" and if number is divisible by both 3 and 5 print "FizzBuzz"

