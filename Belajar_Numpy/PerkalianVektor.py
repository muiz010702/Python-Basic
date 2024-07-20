import numpy as np

m = np.array([3,2])
g = np.array([8,5])

# perkalian dot
w = np.dot(m,g)
print(w)

# perkalian verktor
A = np.array([3,6,5])
B = np.array([2,8,3])

C = np.cross(A,B)
C1 = np.cross(B,A)
print(C1)