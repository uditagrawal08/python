from statistics import mean
from scipy import stats
estimates=[522,552,325,327,985,210,520,100,302,520,410,2580]
estimates.sort()
for i in range(len(estimates)): 
    print(estimates[i])
tv=int(0.1*len(estimates))
new=estimates[tv:(len(estimates)-tv)]
print(new)    
print(mean(new))
#or we can use stats .trim mean 
s=stats.trim_mean(estimates,0.1)
print(s)