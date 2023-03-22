import matplotlib.pyplot as plt
estimates=[100,200,300,4,4,50,660,720,900,3,21,84,78,95]
y=[]
for i in range(len(estimates)):
    y.append(i)
estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:]   
estimates=estimates[:len(estimates)-tv]  
y=y[tv:len(y)-tv]  

plt.hist(estimates,bins=20)
plt.show()