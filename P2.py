n1=0;
n2=1;
nextNum=0;
theSum=0;
while nextNum<4000000:
    nextNum=n1+n2;
    n1=n2;
    n2=nextNum;
    if(nextNum%2==0):
        theSum=theSum+nextNum;
print(theSum);