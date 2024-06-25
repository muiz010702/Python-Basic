import numpy as np

A = np.array(([1,2],
              [3,4]))

B = np.ones(([2,2]))

print("matriks a")
print(A)

print("matriks b")
print(B)

# perkalian matrix
C = np.dot(A,B)
print(C)
