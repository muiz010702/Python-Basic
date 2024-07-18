import numpy as np
#array
A = np.array([1,2,3])
B = np.array([4,5,7])

#stacking matrix atau menumpuk matrix

C = np.hstack((B,A))
D = np.vstack((A,B))

print(D)

#matrix

M1= np.zeros((2,3))
M2 = np.ones((2,3))

Mat1 = np.hstack((M1, M2))

print(Mat1)