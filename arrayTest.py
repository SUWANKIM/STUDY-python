import numpy as np

row, col = 3,4
li = [[kk + 1+ jj*col for kk in range(col)] for jj in range(row)]
np1 = np.array(li)

np2 = np.zeros((np1.shape[0]+2, np1.shape[1]+2))
np2[1:-1,1:-1] = np1

np2[0] = np2[1]
np2[-1] = np2[-2]
np2[:,0] = np2[:,1]
np2[:,-1] = np2[:,-2]
print(np2)
