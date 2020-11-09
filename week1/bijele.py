k,q,r,b,kn,p=map(int,input().split())
if k>1 or k<=1:
    k=1-k
if q>1 or q<=1:
    q=1-q
if r>2 or r<=2:
    r=2-r
if b>2 or b<=2:
    b=2-b
if kn>2 or kn<=2:
    kn=2-kn
if p>8 or p<=8:
    p=8-p
    
print(k,q,r,b,kn,p)
