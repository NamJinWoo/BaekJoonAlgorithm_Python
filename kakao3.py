import numpy as np

from skimage.util import view_as_windows

def solution(key, lock):
    answer = True
    lock = np.pad(lock, pad_width=len(key[0])-1, mode='constant', constant_values=0)
    # print(lock)
    # print(lock[3][3])
    # print("----------------------")
    rotated90 = np.array(zip(*key[::-1]))
    # print(list(rotated90))
    windows = view_as_windows(lock, rotated90.shape)
    print((windows == rotated90).all(axis=(2,3)).any())
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])