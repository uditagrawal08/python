import random
import string
symbol=[]
symbol=list(string.ascii_letters)
cards1=[0]*5
cards2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbol=random.choice(symbol)
symbol.remove(samesymbol)
print(samesymbol)
print(symbol)
if(pos1==pos2):
    cards1[pos1]=samesymbol
    cards2[pos1]=samesymbol
else:
    cards1[pos1]=samesymbol
    cards2[pos2]=samesymbol
    #yaha per cards 2 cards 1 ke liye same symbols nhi hataye hai because i dont find it necessary
    #ask to r.v then implemeet
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        cards1=random.choice(symbol)
        symbol.remove(cards1)
        cards2=random.choice(symbol)
        symbol.remove(cards2)        
        i=i+1
print(cards1)
print(cards2)



