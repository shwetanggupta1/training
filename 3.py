def fib(n):
    a=0
    b=1
    sum=0

    while sum<n:
        yield sum
        a=b
        b=sum
        sum=a+b

x=fib(5)

print(x.__next__())
print(x.__next__())
print(x.__next__())
