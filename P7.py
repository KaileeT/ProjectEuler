count=1;
theNum=2;
thePrime=0;
isPrime=0;
while count<10002:
    for x in range(2,theNum):
        if(theNum%x==0 and x!=theNum):
            isPrime=0;
            break;
        else:
            isPrime=1;
    if(isPrime==1 or theNum==2):
        thePrime=theNum;
        count=count+1;
    theNum=theNum+1;
print(thePrime);