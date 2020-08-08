
t = int(input())
count = [1,2,4]
for i in range(3, 11):
    count.append(count[i-1]+count[i-2]+count[i-3])
for j in range(t):
    n = int(input())
    print(count[n-1])


    