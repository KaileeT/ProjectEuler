sumSquares=0;
squareSum=0;
for x in range(1,101):
    sumSquares=sumSquares+(x*x);
for y in range(1,101):
    squareSum=squareSum+y;
squareSum=squareSum*squareSum;
if(sumSquares>squareSum):
    print(sumSquares-squareSum);
else:
    print(squareSum-sumSquares);