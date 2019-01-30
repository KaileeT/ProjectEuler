theNum=2000000;
theSum=0;
primeNums=[0]*(theNum+1);
for x in range(0,theNum,2):
    primeNums[x]=0;
for y in range(3,theNum,2):
    primeNums[y]=1;
primeNums[1]=0;
primeNums[2]=1;
for i in range(3,theNum,2):
    if(i*i<=theNum):
        if(primeNums[i]==1):
            for j in range(i,theNum):
                if(i*j<=theNum):
                    # print(i,j);
                    primeNums[i*j]=0;
for k in range(2,theNum):
    if(primeNums[k]==1):
        theSum=theSum+k;
print(theSum);