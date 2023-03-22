
import random

def choose():
    words=["rainbow","winter","summer","hello","world","mylove","work","passion","funky"]
    #random.choice is already defined for pick any word from list
    pick=random.choice(words)
    return pick

def jumble(picked_word):
    #random.sample is already defined for pick any word from word letters
    jumbled="".join(random.sample(picked_word,len(picked_word)))
    return jumbled
 

def thank(play1,play2,ppl1,ppl2):

    print(play1,"thank for play your score is",ppl1)
    print(play2,"thank for play your score is",ppl2)


def play():
    play1=input("enter name of 1st player")
    play2=input("enter name of 2st player")
    pp1=0
    pp2=0
    temp=0
    while(1):
    #compurter choose

        picked_word=choose()
    #create question from computer
        que=jumble(picked_word)
        print(que)
        if(temp%2==0):
            print(play1,"your  chance")
            ans=input("what is in your mind")
            if(ans==picked_word):
                pp1=pp1+1
                print("your score is",pp1)
            else:    
                print("better luck next time")
            c=int(input("press 1 for continue else 0"))
            if(c==0):
                thank(play1,play2,pp1,pp2)
                break
        else:
                print(play2,"your  chance")
                ans=input("what is in your mind")
                if(ans==picked_word):
                    ppl2=ppl2+1
                    print("your score is",pp2)
                else: 
                    print("better luck next time")
                c=int(input("press 1for continue else press 0"))
                if(c==0):
                    thank(play1,play2,pp1,pp2)
                    break

    