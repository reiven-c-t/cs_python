import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(a)
print(a.flags)
#C_Contiguous C配列型でデータがメモリ上で連続しているかどうか
#F_Contiguous Fortran配列型

print(a.ndim)
# 次元数
print(a.size)
# 要素数
print(a.shape)
# 要素数（行数、列数）

b = np.zeros([2,3])
print(b)

c = np.ones([4,4])
print(c)

d = np.identity(4)
print(d)

print(np.arange(10))

print(np.arange(1,10,1))

print(np.linspace(1,10,10))

