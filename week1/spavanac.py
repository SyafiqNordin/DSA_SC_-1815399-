h,m=map(int,input().split())

if m<45:
    m=m+60
    if h==0:
        h=h+23
    else:
        h=h-1

m=m - 45
print(h,m)
