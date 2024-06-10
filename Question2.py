import numpy as np

# Compute the eigenvalues and right eigenvectors
matrix = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
