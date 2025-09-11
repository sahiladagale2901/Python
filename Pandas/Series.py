# Series -> one dimensional Data set

import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 6])
print("Series\n", data)

###############################################################################

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

data = pd.Series(d)
print("Dictionary Series\n", data)

###############################################################################

li = [10, 20, 30, 40]
index = ['a', 'b', 'c', 'd']

data = pd.Series(li, index=index)
print("Indexing Series\n", data)
