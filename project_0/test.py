#a = 4678678678
#b = 4678678678
#import numpy as np
#a = np.int64(a)
#b = np.int64(b)
#c = a + b
#print(2**32 - 1)

def shuffle_seed(array):
    import numpy as np
    a = np.random.randint(0,4294967296, dtype=np.int64)
    np.random.seed(a)
    shuffle_seed = np.random.permutation(array)
    return shuffle_seed, a

array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# (array([1, 3, 2, 4, 5]), 2332342819)
#shuffle_seed(array)
# (array([4, 5, 2, 3, 1]), 4155165971)