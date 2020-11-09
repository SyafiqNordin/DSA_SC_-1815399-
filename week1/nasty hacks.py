n= int(input())
for i in range(n):
    r,e,c=map(int,input().split())
    ans=e-c
    if ans==r:
        print("does not matter")
    elif ans<r:
        print("do not advertise")
    elif ans>r:
        print("advertise")
