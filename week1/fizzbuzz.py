x,y,n=map(int,input().split())

for i in range(n):
    if (i+1)%x==0 and (i+1)%y==0:
        print("FizzBuzz")

    elif (i+1)%x==0:
        print("Fizz")

    elif (i+1)%y==0:
        print("Buzz")

    else:
        print(i+1)
