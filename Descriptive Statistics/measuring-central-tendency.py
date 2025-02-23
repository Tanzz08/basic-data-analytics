import numpy as np
from scipy import stats

# Mean
jumlah_kucing = np.array([3,2,1,1,2,3,2,1,0,2])
print(f"Mean dari data: {jumlah_kucing.mean()}")

# Median 
print(f"Median dari data: {np.median(jumlah_kucing)}")

# Mode
mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print(f"Mode dari data: {mode_jumlah_kucing}")


