import numpy as np

x_mat = np.mat([[0, ], [0, ]])

f_mat = np.mat([[1, 1], [0, 1]])
m = f_mat*x_mat
print(m)