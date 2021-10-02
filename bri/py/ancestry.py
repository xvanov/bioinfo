# code not tested - need data with SNPs of genotypes
# see: https://www.internationalgenome.org/data/

import required Python libraries and genotypes dataset
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
labels=np.load("data/labels.npy")
genotypes=np.load("data/foo.npy")

# Create a new PCA object.
pca = PCA(n_components=3)

# Find three principal components, and project the dataset onto them
genotypes_fit = pca.fit_transform(genotypes)
sample = np.load("data/sample.npy")
sample_proj = pca.transform(sample)

# Plot the dataset projected onto the two principal directions with labels
for i in range(len(labels)):
    if labels[i] == 'LWK':
        color='green'
        lwk=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
    elif labels[i] == 'YRI':
        color='purple'
        yri=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
    elif labels[i] == 'MSL':
        color='orange'
        msl=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
    elif labels[i] == 'ESN':
        color='blue'
        esn=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
    elif labels[i] == 'GWD':
        color='black'
        gwd=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)

        

plt.scatter(sample_proj[0][1], sample_proj[0][0], c='red', marker='X', s = 500)


# Create a legend
plt.legend((lwk,yri,msl,esn,gwd),['Luhya in Webuye, Kenya',
                                             'Yoruba in Ibadan, Nigeria','Mende in Sierra Leone',
                                             'Esan in Nigeria','Gambian in Western Divisions'], scatterpoints=1, 
                                               loc='upper right',ncol=1,fontsize=8)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.savefig('pca.png')
