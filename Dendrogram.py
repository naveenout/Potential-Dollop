#Visualization with hierarchical clustering @ Unsupervised Learning,
#Simple Example to Undestand the Concept
#sample array only to undestand the concept

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np

sample=np.array([[5.26,14.84,0.871,5.763,3.312,2.221,5.22],
                [14.88,14.57,0.8811,5.554,3.333,1.018,4.956],
                [14.29,14.09,0.905,5.291,3.337,2.699,4.825],
                [13.84,13.94,0.8955,5.324,3.379,2.259,4.805],
                [16.14,14.99,0.9034,5.658,3.562,1.355,5.175],
                [14.38,14.21,0.8951,5.386,3.312,2.462,4.956],
                [14.69,14.49,0.8799,5.563,3.259,3.586,5.219],
                [14.11,14.1,0.8911,5.42,3.302,2.7,5],
                [6.63,15.46,0.8747,6.053,3.465,2.04,5.877],
                [16.44,15.25,0.888,5.884,3.505,1.969,5.533],
                [15.26,14.85,0.8696,5.714,3.242,4.543,5.314]])

# Perform the necessary imports
list123=['sample1','sample2','sample3','sample4','sample5','sample6','sample7','sample8','sample9','sample10','sample11']

# Calculate the linkage: mergings
mergings = linkage(sample,method='complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,labels=list123,leaf_rotation=90,leaf_font_size=6,)
plt.xlabel("Samples")
plt.ylabel("Values")
plt.show()
