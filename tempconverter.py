temp=int(input())
x=input()
if (x=='C'):
    f=(9/5)*temp +32
    print(f,"F")
    k=temp+273
    print(k,"K")
if (x=='F'):
    c=(5/9)*(temp-32)
    print(c,"C")
    k=c+273
    print(k,"K")
if (x=='K'):
    c=temp-273
    print(c,"C")
    f=(9/5)*(temp-273)+32
    print(f,"F")
