import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    ex=12
    # Generates random poisson distribution 
    _ = np.random.poisson(ex,size=1000)
    # labels and title for histogram
    plt.xlabel('poisson distributions')
    plt.ylabel('Probability') 
    plt.title('Histogram for Random Poisson Distribution')
    # Generates a histogram using the above data
    bins=plt.hist(_,20,density=True,color='g')
    # Displays the histogram
    plt.show()
