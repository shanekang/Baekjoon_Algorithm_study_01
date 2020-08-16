x,y = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x,y)


print(f'{gcd(x,y)}\n{int(lcm(x,y))}')
