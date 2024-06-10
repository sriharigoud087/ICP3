import numpy as np

# 1. Create a random vector of size 15 with integers in the range 1-20
vector = np.random.randint(1, 21, size=15)
print("Original vector:", vector)

# 2. Reshape the array to 3x5
array_3x5 = vector.reshape(3, 5)
print("Reshaped to 3x5 array:\n", array_3x5)

# 3. Print array shape
print("Shape of the array:", array_3x5.shape)

# 4. Replace the max in each row by 0
for i in range(array_3x5.shape[0]):
    array_3x5[i, np.argmax(array_3x5[i])] = 0
print("Array after replacing max in each row by 0:\n", array_3x5)

# 5. Create a 2D array of size 4x3 (4-byte integer elements), print shape, type, and data type
array_4x3 = np.zeros((4, 3), dtype=np.int32)
print("4x3 Array:\n", array_4x3)
print("Shape of the 4x3 array:", array_4x3.shape)
print("Type of the array:", type(array_4x3))
print("Data type of the array:", array_4x3.dtype)
