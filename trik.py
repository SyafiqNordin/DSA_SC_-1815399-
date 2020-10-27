ans=1
change=input()
size_input=len(change)
for i in range(size_input):
    if change[i]=='A':
        if ans==1:
            ans=2
        elif ans==2:
            ans=1
    elif change[i]=='B':
        if ans==2:
            ans=3
        elif ans==3:
            ans=2
    elif change[i]=='C':
        if ans==1:
            ans=3
        elif ans==3:
            ans=1

print(ans)
