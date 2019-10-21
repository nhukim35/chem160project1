import numpy as np
ntrials=5000
for a in range (1,200):
    sum=0
    for trial in range(ntrials):
        x=np.random.normal(size=a)
        x.sort()
        sum+=x[a-1]
    sum/=ntrials
    print("N=",a,"average sd maximum",sum)