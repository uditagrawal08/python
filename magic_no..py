def magic_square(n):

    magicnumber=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicnumber.append(l);
        print(l)
#magic_square(5)
   
    i=n//2
    j=n-1
    count =1
    num=n*n
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:

            if(i==-1):
                i=n-1
            if(j==n):
                j=0
        
        if(magic_square!=0):
            i=i+1
            j=j-2
            continue;
        else:
            magic_square[i][j]=count
            count+=1
        i=i-1
        j=j+1
 
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j],ends=" ")
        print()

magic_square(5)