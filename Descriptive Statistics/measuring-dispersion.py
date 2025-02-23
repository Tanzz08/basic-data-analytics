import numpy as np
import pandas as pd

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Range -> selesih dari nilai max dan nilai min
range = jumlah_kucing.max() - jumlah_kucing.min()
print(f"Range dari data: {range}")

# Interquartile Range -> selisih dari Q3 dan Q1
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(f"IQR dari data: {iqr}")

# Variance -> rata-rata selisih kuadrat antar titik data dan nilai mean nya
jumlah_kucing_series = pd.Series(jumlah_kucing)
print(f"Variance dari data: {jumlah_kucing.var()}")


# Standard Deviation -> menghitung akar kuadrat dari variance
print(f"Standard Deviation dari data: {jumlah_kucing_series.std()}")


