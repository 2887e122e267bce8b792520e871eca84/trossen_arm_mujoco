import numpy as np

arr_1 = np.array([1,2,3])
arr_2 = np.array([9,8,7])

arr_3 = np.concatenate([arr_1,arr_2])
print(arr_3)
arr_3[0]=1000
print(arr_3)