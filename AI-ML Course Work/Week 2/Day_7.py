import numpy as np

# Topics example problem
arr = np.array([1,2,3,4,5])
print(arr)

zeros = np.zeros((2,3))
print(zeros)

rand = np.random.randint(1,10,5)
print(rand)

# task
array = np.array([5,4,3,2,1])
print(array)

ones = np.ones((3,3))
print(ones)

rand = np.random.randint(1,100,4)
print(rand)

# Topics example problem
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

# task
b = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,0]])
print(b.shape)
print(b.size)
print(b.ndim)

# task
c = np.array([[1.1,2.2,3.3,4.4],[4.4,5.5,6.6,7.7]])
print(c.dtype)

# Topics example problem
b = np.array([3,7,1,9,4])
print(b.reshape(5, 1))
print(b.max(), b.min())
print(b.argmax(), b.argmin())

# task
c = np.array([3,7,1,9,4,5])
print(c.reshape(2,3))
# task
rand = np.random.randint(1,50,8)
print(c.max(), c.min())
print(c.argmax(), c.argmin())

# Topics example problem
c = np.array([1,2,3])
c_copy = c.copy()
c_copy[0] = 100
print(c, c_copy)

d = np.array([1,2,3])
print(np.append(d, [4,5]))
print(np.insert(d, 1, 100))

# task
t1 = np.array([2,4,6,8,9])
t_copy = t1.copy()
t_copy[4] = 10
print(t1, t_copy)
# task
t2 = np.array([2,4,6,8,10])
print(t2.append(t2,[12,14,16]))
print(t2.insert(t2, 2, 100))

# Topics example problem
e = np.array([5,2,8,1])
print(np.sort(e))
print(np.delete(e, 0))
new_e = np.sort(e)
print(np.delete(new_e, 0))

f1, f2 = np.array([1,2]), np.array([3,4])
print(np.concatenate((f1,f2)))
print(np.array_split(np.arange(1,7),3))

# task
e = np.array([5,2,8,1])
print(np.sort(e))
print(np.delete(e, 1))
# task
f1, f2 = np.array([1,2]), np.array([3,4])
print(np.concatenate((f1,f2)))
print(np.array_split(np.arange(1,7),2))

# Data loading and saving
arr = np.array([1,2,3,4])
np.save('my_array.npy', arr)

loaded = np.load('my_array.npy')
print(loaded)

# tasks...

# Topics example problem
g = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(g[1,2])
print(g[g>5])

# task
g = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(g[2,1])
print(g[g>5])

# Broadcasting
h = np.array([1,2,3,4,5])
print(h + 10)

result = [x + 10 for x in h]
print(result)

# task
h = np.array([1,2,3,4,5])
print(h + 100)
# task
part_1 = [3*x for x in h]
part_2 = [x - 1 for x in h]
print(part_2)

# Type Casting and Arthmetic ops
i = np.array([1.5, 2.7, 3.1])
print(i.astype(int))

j = np.array([1,2,3])
k = np.array([4,5,6])
print(j + k, j - k, j * k)
print(j / k, j ** 2)

# task
i = np.array([1.5, 2.7, 3.1])
print(i.astype(int))
# task
j = np.array([1,2,3,4])
k = np.array([4,5,6,7])
print(j + k, j - k, j * k,j / k)

# Universal array function
m = np.array([1,4,9,16])
print(np.sqrt(m))

n = np.array([1,2])
print(np.exp(n))

# task
m = np.array([49,81,64,625,25])
print(np.sqrt(m))
# task
n = np.array([34,65,23,54,97])
print(np.sin(n))