import random
movie=["hello world","sanjay dutt"]
choices=random.choice(movie)
letters=list(choices)
print(choices)
print(letters)
temp=[]
n=len(choices)
for i in range(n):
    if(letters[i]==' '):
        temp.append(" ")
    else:
        temp.append("*")
print(temp)

print(choices)
print(letters)
qn="".join(str(x) for x in temp)
print(qn)