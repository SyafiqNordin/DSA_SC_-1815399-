a,b=map(int,input().split())
revA,revB=0,0

while a and b !=0:
    digitA=a % 10
    digitB=b %10
    revA = revA *10+digitA
    revB=revB*10+digitB
    a=a//10
    b=b//10
print(max(revA,revB))
