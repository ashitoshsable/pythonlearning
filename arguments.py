def func(a,**b):
    print(a)
    for i,j in b.items():
        print(i,end=' ')
        print(j)

func("Ashitosh",d='key',e='ball',c='tall')

