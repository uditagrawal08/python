def binary(a,num):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    while(first_pos<last_pos and flag==0):
        mid=(first_pos+last_pos)//2
        if(num==a[mid]):
            flag=1
            print("emement is present  "+str(num))
            return
        elif(num<a[mid]):
            last_pos=mid-1
        elif(num>a[mid]):
            first_pos=mid+1
    print("element is not present")

a=[]
for i in range(1,500):
    a.append(i)
print(a)
binary(a,50)
