n=20;
isAns=0;
while isAns==0:
    for x in range(11,20):
        if(n%x!=0):
            isAns=0;
            n=n+1;
            break;
        else:
            isAns=1;
print(n);