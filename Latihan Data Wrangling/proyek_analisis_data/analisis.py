import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
Assessing Data
"""
# Membuat tabel customers
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()
customers_df.info()
print(customers_df.isna().sum())

# Load tabel orders
order_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
order_df.head()
print("Jumlah duplikasi: ", order_df.duplicated().sum())
print(order_df.describe())

# Membuat table product
product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()
product_df.info()
print("Jumlah duplikasi :", product_df.duplicated().sum())
print(product_df.describe())

# Load tabel sales 
sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()
sales_df.info()
print(sales_df.isna().sum())
print("Jumlah duplikasi:", sales_df.duplicated().sum())
print(sales_df.describe())


"""
Cleaning Data
"""
# Menghilangkan duplicate data
customers_df.drop_duplicates(inplace=True)
print("Jumlah duplikasi :", customers_df.duplicated().sum())

# Menangani missing value

# 1. filtering
print(customers_df[customers_df.gender.isna()])

# 2. Imputation - identifikasi nilai dominan karena data gender merupakan kategorik
print(customers_df.gender.value_counts())

# 3. setelah identifikasi nilai dominan, gunakan method fillna untuk mengganti missing values
customers_df.fillna(value="Prefer not to say", inplace=True)
imputation_result = customers_df.isna().sum()
print(imputation_result)

# Menangani inaccurate value 

# 1. filtering 
print(f"Filtering max age: \n {customers_df[customers_df.age == customers_df.age.max()]}")

# 2. replace inaccurate data karna human error
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)
print(f"Filtering max age: \n {customers_df[customers_df.age == customers_df.age.max()]}")
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)

print(customers_df.describe())

'''
Clearing Data - Order
'''

# Mengganti tipe data yang bermasalah menggunakan function to_datetime()
datetime_columns = ["order_date", "delivery_date"]

for column in datetime_columns:
    order_df[column] = pd.to_datetime(order_df[column])

order_df.info()

'''
Clearing Data - Product
'''

product_df.drop_duplicates(inplace=True)
print("Jumlah duplikasi pada kolom product:", product_df.duplicated().sum())

'''
Clearing Data - sales
'''

# identifikasi missing value
print(sales_df[sales_df.total_price.isna()])

sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]

print(sales_df.isna().sum())


