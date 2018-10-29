import numpy as np
import matplotlib.pyplot as plt
x,fr=0,0.3
n= np.random.normal(x,fr,1000)
c=12
p= np.random.poisson(c,1000)
data= []
for i in range(100):
    r=np.random.randint(0,1000)
    avg=(p[r]+n[r])
    avg=avg/2
    data.append(avg)
plt.xlabel("Data")
plt.ylabel("Probability")
plt.title('Histogram for Average of both Random and poisson')
plt.hist(data,20,density=True,color='g')
plt.show()
