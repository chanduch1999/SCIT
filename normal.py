import matplotlib.pyplot as plt
import numpy as np

for i in range(3):
    # Generates a random distribution,location : mean of the distribution, scale : width of the distribution,size : output shape
    _ = np.random.normal(location=0,scale=0.3,size=1000)
    # Lables and title for Histogram
    plt.xlabel('normal distrbution')
    plt.ylabel('probability')
    plt.title('Histogram for Random Normal Distribution')
    # Generates the Histogram for above data
    bins = plt.hist(_,20,density=True,color='g')
    # Displays the Histogram
    plt.show()

