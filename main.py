import numpy as np

if __name__ == '__main__':
    x0 = [[1,2],[2,3],[3,4],[4,5]]
    x = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]])
    y = np.transpose(x)
    z = x @ y
    print(x0)
    print(x[(0, 1)])
    print(y)
    print(x < y)
