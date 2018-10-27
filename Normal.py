import matplotlib.pyplot as plt
import numpy as np

for i in range(3):
    x,fr=0,0.3
    _ = np.random.normal(x,fr,1000)
    plt.xlabel('normal distrbution')
    plt.ylabel('probability')
    plt.title('Histogram for Random Normal Distribution')
    bins = plt.hist(_,20,density=True,color='g')
    plt.show()

