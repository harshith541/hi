import numpy as np

a = np.array([10, 20, 30, 40, 50])

result = a[(a < 20) | (a > 40)]

print(result)