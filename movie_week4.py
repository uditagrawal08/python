import random
movie=["avenger","dangal","hero","welcome","tarre zamin per","i love my india"]

def create_question(movie):
    temp=[]
    n=len(movie)
    letters=list(movie)
    for i in range (n):
        if(letters[i]==" "):
            temp.append(" ")
        else:
            temp.append("*")
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    #print(letter)
    #print("here")
#    print(c)
    if(c==0):
        return False
    else:
       return True


def unlock(qn,picked_movie,letter):
    temp=[]

    n=len(picked_movie)
    letters=list(picked_movie)
 #   print(letter)
    for i in range (n):
        if(letters[i]==letter):
            temp.append(letter)
        else:
            temp.append(qn[i])
    modified_qn="".join(str(x) for x in temp)
    return modified_qn




def play():
    play1=input("enter the name of first play")
    play2=input("enter the name of second play")
    ppl1=0
    ppl2=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            print(play1,"your tern")
            picked_movie=random.choice(movie)
            qn=create_question(picked_movie)
            print (qn)

            not_said=True
            while(not_said):
                letter=input("input letter")
  #              print(letter,"your letter is...........")
                if(is_present(letter,picked_movie)):
                  #  print("idhar")
                    modified_qn=unlock(qn,picked_movie,letter)
                    qn=modified_qn
                    print(modified_qn)
                    d=input("press 1 for guess movie name..2 for unlock another letter ")
                        #unlock
                    if(d=="1"):
                        ans=input("movie name is")
                        if(ans==picked_movie):
                            ppl1+=1
                            print("correct guess")
                            not_said=False
                        else:
                            print("wrong ans")    


                else:
                    print(letter,"not present")

            c=input("do y want to continue press 1 else press 0")
            if(c=="0"):
                print(play1," your score is",ppl1)        
                print(play2," your score is",ppl2)
                willing=False      
            turn+=1
        else:#player 2
            
            print(play2,"your tern")
            picked_movie=random.choice(movie)
            qn=create_question(picked_movie)
            print (qn)

            not_said=True
            while(not_said):
                letter=input("input letter")
  #              print(letter,"your letter is...........")
                if(is_present(letter,picked_movie)):
                  #  print("idhar")
                    modified_qn=unlock(qn,picked_movie,letter)
                    qn=modified_qn
                    print(modified_qn)
                    d=input("press 1 for guess movie name..2 for unlock another letter ")
                        #unlock
                    if(d=="1"):
                        ans=input("movie name is")
                        if(ans==picked_movie):
                            ppl2+=1
                            print("correct guess")
                            not_said=False
                        else:
                            print("wrong ans")    


                else:
                    print(letter,"not present")

            c=input("do y want to continue press 1 else press 0")
            if(c=="0"):
                print(play1," your score is",ppl1)        
                print(play2," your score is",ppl2)
                willing=False      
            turn+=1
play() 