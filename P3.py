theNum=600851475143;
div=2;
while theNum!=0:
    if(theNum%div!=0):
        div=div+1;
    else:
        theNum=theNum/div;
        if theNum==1:
            break;
print(div);