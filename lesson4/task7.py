def fact(n):
    f=1
    for i in range(1,n):
        f=f*i
        yield f

print(*[f for f in fact(10)])
