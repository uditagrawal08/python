import random

# # for i in range(3):

# #     for j in range(2,i-1,-1):
# #         print("hello")
# x=random.randint(0,2)
# print(x)
door=[]

goat_door=[]
swap=0
not_swap=0
play=True
while(play==True):
    x=random.randint(0,2)
    for i in range(0,3):
        if(i==x):
            door.append("bmw")
        else:
            door.append("goat")
            goat_door.append(i)
    print(door)
    print(goat_door)
    print("enter the choice y want to open")
    choice=int(input(" 0 for 1st door ...\n1 for 2nd door ...\n2 for 3rd door\n"))
    door_open=random.choice(goat_door)
    while(door_open==choice):
        door_open=random.choice(goat_door)
    print("your new door  open i.e.  \n",door_open)
    print("your new door  open contain ")
    print("do you want to swap to another door")
    ask=int(input("enter 0 to swap else 1"))
    if(ask==0):
        new_choice=random.randint(0,2)
        while(new_choice==choice or new_choice==door_open):
            new_choice=random.randint(0,2)
        print("your new choice open door of",door[new_choice])
        if(new_choice==x):
            print("y win")
            swap=swap+1
        else:
            print("y loss")
    else:
        if(choice==x):
            print("y win")
            not_swap=not_swap+1
        else:
            print("y loss")



#     if(choice==x):
#         print('y won a "bmw"')
#         exit()
#     else:
#         print("y want to swap")
#         new_choice=int(input("enter 0 for yes and 1 for No"))
#         if(new_choice==0):
#             print("enter new choice another than previous")
#             another_choice=int(input())
#             if(another_choice==x):
#                 print('y won a "bmw"')
#                 swap=swap+1
               

#             else:
#                 print("you losss")
#         if(new_choice==1):
#             print("y lost")
#             not_swap=not_swap+1
#     print("do y want to continue")
#     cont=input("press t for yes else N")
#     if(cont=="t"):
#         play=True
#     else:
#         play=False
# print(swap)
# print(not_swap)
    





