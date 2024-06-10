import numpy as np



# Reshape an array without changing its data
initial_array = np.array([[1, 2], [3, 4], [5, 6]])
reshaped_array = initial_array.reshape(2, 3)
print("Initial array:\n", initial_array)
print("Reshaped array to 2x3:\n", reshaped_array)
