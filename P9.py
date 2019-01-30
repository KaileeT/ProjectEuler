theSum=1000;
theProd=0;
for x in range(3,theSum):
    c=theSum-x;
    for y in range(2,c):
        b=y;
        for i in range(1,b):
            a=i;
            if((a*a)+(b*b)==(c*c) and a+b+c==theSum):
                print(a,b,c);
                theProd=a*b*c;
print(theProd);