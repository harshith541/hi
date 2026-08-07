import numpy as np

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

row_indices = [0, 2]
col_indices = [1, 2]

print(b[row_indices, col_indices])