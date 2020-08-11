def hanoi(n, start, middle, end):
    if n == 1:
        count.append([start, end])
    
    else:
        hanoi(n-1, start, end, middle)
        count.append([start, end])
        hanoi(n-1, middle, start, end)

count = []
hanoi(int(input()),1,2,3)

print(len(count))
print("\n".join([' '.join(str(i) for i in row) for row in count]))
