import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Distribusi Data
plt.hist(jumlah_kucing, bins=4)
plt.show()

# Skewness -> untuk mengukur kesimetrisan sebuah distribusi data
jumlah_kucing_series = pd.Series(jumlah_kucing)
print(f"Skewness dari data: {jumlah_kucing_series.skew()}")

