from collections import Counter
n = 10
modulo = 0
num = []
distinct_num = 0

for i in range(n):
    num.append(int(input()))
    modulo = num[i] % 42
    num[i] = modulo

distinct_num = (Counter(num).keys())
print(len(distinct_num))
