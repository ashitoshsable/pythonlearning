a=10

def func():
    a=5
    x=globals()['a']

    print(id(x))

func()
print(id(a))

