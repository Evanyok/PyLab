import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([(1,2,3),(4,5,6)])
arr3 = np.zeros([2,3])
arr4 = np.ones([2,2])
arr5 = np.identity(3) 
arr6 = np.random.random(size=(3,3))
arr8 = np.eye(3)

print(arr2.shape)
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype.name)
print(type(arr2))

f = lambda x, y: 10 * x + y
arr7 = np.fromfunction(f, (2,3), dtype= int)
print(arr7)

for elem in arr7.flat:
    print(elem)



# common functions
# np.exp 指数
# np.sqrt 开方
# np.sin cos tan ...
# np.add 
# np.vstack(arr1, arr2) 纵向合并
# np.hstack(a1, a2)
# np.vsplit(arr, parts) 纵向分割
# np.hsplit(arr, parts)
# np.empty
# np.all 测试所有元素为True
# np.any 测试至少一个为True
# np.average
# np.nonzero 非零元素位置
# np.sort
# np.var 方差
# np.where 返回满足条件的元素
# np.reshape
# np.eye 
# np.transpose 转置
# np.std 标准差
# np.cov 加权协方差矩阵