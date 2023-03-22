def fact(n):
    if (n<=1):
        return 1
    else:
        return n*fact(n-1)

print("enter a no.")
n=int(input())
print(fact(n))