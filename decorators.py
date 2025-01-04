def div(a,b):
    return a/b

def ddiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=ddiv(div)

print(div(2,4))