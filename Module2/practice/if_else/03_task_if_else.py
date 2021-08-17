a = int(input())
b = int(input())
c = int(input())
if a + b < c or b + c < a or a + c < b:
    if (a == b or c) or (b == c)  or (c == a):
        print("YES")
    else:
        print("NO")
else:
    print("error")
