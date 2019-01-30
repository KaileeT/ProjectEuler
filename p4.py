from numpy import size
from __builtin__ import str
from _ast import Str
n1=999;
n2=999;
isPalindrome=0;
largestPalindrome=0;
while n1>99:
    theNum=n1*n2;
    numStr=str(n1*n2);
    for x in range(len(numStr)/2):
        if(numStr[x]!=numStr[len(numStr)-1-x]):
            isPalindrome=0;
            break;
        else:
            isPalindrome=1;
    if(isPalindrome==1):
        if(theNum>largestPalindrome):
            largestPalindrome=theNum;
    else:
        while n2>99:
            theNum=n1*n2;
            numStr=str(n1*n2);
            for y in range(len(numStr)/2):
                if(numStr[y]!=numStr[len(numStr)-1-y]):
                    isPalindrome=0;
                    break;
                else:
                    isPalindrome=1;
            if(isPalindrome==1):
                if(theNum>largestPalindrome):
                    largestPalindrome=theNum;
            n2=n2-1;
    n1=n1-1;
    n2=999;
print(largestPalindrome);