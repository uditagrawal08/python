from PIL import Image
import random

def check_ladder(points):
    if (points==8):
        print("ladder")
        return 26
    if (points==21):
        print("ladder")
        return 82
    if (points==43):
        print("ladder")
        return 77
    if (points==50):
        print("ladder")
        return 82
    if (points==43):
        print("ladder")
        return 77
    if (points==50):
        print("ladder")
        return 91
    if (points==54):
        print("ladder")
        return 93
    if (points==62):
        print("ladder")
        return 96
    if (points==66):
        print("ladder")
        return 87
    if (points==80):
        print("ladder")
        return 100
    else:
        return points

def check_snake(points):
    if(points==44):
        print("snake")
        return 22
    elif(points==46):
        print("Snake")
        return 5
    elif(points==48):
        print("Snake")
        return 9
    elif(points==52):
        print("Snake")
        return 11
    elif(points==55):
        print("Snake")
        return 7
    elif(points==59):
        print("Snake")
        return 17
    elif(points==64):
        print("Snake")
        return 36
    elif(points==69):
        print("Snake")
        return 33
    elif(points==73):
        print("Snake")
        return 1
    elif(points==83):
        print("Snake")
        return 19
    elif(points==92):
        print("Snake")
        return 51
    elif(points==95):
        print("Snake")
        return 24
    elif(points==98):
        print("Snake")
        return 28
    else:
        return points
    
    
    
    
    
    
def play():
    play1=input("enter y name 1")
    play2=input("enter y name 2")
    pl1=0
    pl2=0
    turn =0
    
    img=Image.open("snake.jpg")
    img.show()
    while(1):
        if(turn%2==0):
            print("play 1 your tern")
            choice=int(input(" do you want to continue press 1 and 0 to exit"))
            if(choice==0):
                exit(0)
            else:
                dice=random.randint(1,6)
                print("dice no. is ",dice)

                pl1=pl1+dice
                pl1=check_ladder(pl1)
                pl1=check_snake(pl1)
                print(play1,"you are at",pl1)
                if(pl1>100):
                    print("Now you want accurate no. to win")
                    pl1=pl1-dice
                 
                
                if(pl1==100):
                    print("you won")
                    exit(0)
        else:
            print("play 2 your tern")
            choice=int(input(" Do you want to continue press 1 and 0 to exit"))
            if(choice==0):
                exit(0)
            else:
                dice=random.randint(1,6)
                print("Dice no. is ",dice)

                pl2=pl2+dice
                pl2=check_ladder(pl2)
                pl2=check_snake(pl2)
                print(play2,"you are at",pl2)


                if(pl2>100):
                    print("Now you want accurate no. to win")
                    pl2=pl2-dice


                if(pl2==100):
                    print("you won")
                    exit(0)
        turn=turn+1    
play()

