import math
n=int(input())
for i in range(n):
    v,t,x,h1,h2=map(float,input().split())
    time=x/(v * (math.cos(math.radians(t))))
    y=(v * time *(math.sin(math.radians(t))))-(0.5 * 9.81 * time * time)

    if y>(h1+1) and y<(h2-1):
        print("safe")
    else:
        print("not safe")
