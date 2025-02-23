import pandas as pd

sampel_data = {
    'name': ['john', 'Alia', 'Anaya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}

df = pd.DataFrame(sampel_data)

# Correlation -> mengidentifikasi korelasi dari dua feature numerik dalam sebuah data
print(df.corr(numeric_only=True))

# Covariance -> mengidentifikasi hubungan antar dua feature dalam sebuah dataset
print(df.cov(numeric_only=True))


