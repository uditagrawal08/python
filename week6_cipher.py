import string
print(string.ascii_letters)
new=open("new_out.txt","w")
dict={}
data=""
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("cipher.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        print(data)
        new.write(data)
new.close()
# f= open("cipher.txt","r")
# print(f.read(5))
# print(f.readline())
# for x in f:
#     print(x.replace("a","5"))