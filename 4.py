def area(name):
    name=name.lower()

    if name=='square':
        a=int(input('enter side of square: '))

        return a*a
    
    if name=='rectangle':
        l=int(input('Enter length of rectangle: '))
        b=int(input('Enter breadth of rectangle: '))

        return l*b

name=input()

print('Area of',name,'is',area(name))

