conv_factor={}
conv_factor['dollar']=50
conv_factor['euro']=100
print(conv_factor)

print(conv_factor['euro'])
print(conv_factor.keys())
print(conv_factor.values())
#print(conv_factor.__init_subclass__(5))
#conv_factor.pop?

del conv_factor['dollar']
print(conv_factor.items())
