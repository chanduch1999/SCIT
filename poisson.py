import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    c=12
    _ = np.random.poisson(c,1000)
    plt.xlabel('poisson distributions')
    plt.ylabel('Probability')
    plt.title('Histogram for Random Poisson Distribution')
    bins=plt.hist(_,20,density=True,color='g')
    plt.show()

