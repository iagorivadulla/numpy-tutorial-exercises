mport numpy as np

vector = np.zeros(10)
size = vector.itemsize




arr = np.zeros(10)
arr[4] = 1

rang_val = np.arange(10, 50)

reverse = np.arange(0, 10)
reverse = reverse[::-1]

matrix = np.arange(0, 9).reshape((3, 3))


zeros = np.array([1,2,0,0,4,0])
nz = np.nonzero(zeros)[0]
result = [i for i in range(len(zeros)) if i not in nz]


ident_matrix = np.eye(3)

arr = np.random.random(3)

arr = max(np.random.random(10))

arr = np.mean(np.random.random(10))


matrix = np.ones((5,5))
matrix[1:-1,1:-1] = 0

matrix = np.ones((3,3))
padded = np.pad(matrix, pad_width=(1, 1))


diagonal = np.arange(0,9).reshape((3,3))
diagonal = np.diag(diagonal)


chess = np.ones((8,8))
chess[0::2, 0::2] = 0.

print(chess)
