import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 # untuk menampilkan teks dalam format judul
st.title('Belajar Analisis Data')

# menampilkan teks dalam format header
st.header('Pengembangan Dashboard')
#menampilkan teks dalam format subheader
st.subheader('Pengembangan Dashboard')

# menampilkan output dari argument markdown
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# untuk menampilkan sebuah output
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

# menampilkan output teks dalam ukuran kecil 
st.caption('Copyright (c) 2023')

# menampilkan potongan code
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

 
 # menampilkan normal text
st.text('Halo, calon praktisi data masa depan.')

# digunakan untuk menampilkan elemen teks latex
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

 # dataframe() - merupakan function yang digunakan untuk menampilkan dataframe sebagai tabel interaktif
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

# table() - digunakan untuk menampilkan data dalam bentuk static table
st.table(data=df)

# metric() - membantu kita untuk menampilkan sebuah metrik tertentu beserta detailnya seperti label, value serta besar perubahan nilainya
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# json - untuk menampilkna data dalam format JSON 
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# pyplot() - digunakan untuk menampilkan grafik visualisasi data yang dibuat menggunakan matplotlib
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)



