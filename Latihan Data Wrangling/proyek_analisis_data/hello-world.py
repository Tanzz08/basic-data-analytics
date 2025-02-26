import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
 
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

# text_input() - untuk memperolah inputan berupa single line text
name = st.text_input(label="Nama lengkap", value='')
st.write('Nama ', name)

# text_area() - memungkinkan unutuk menginput multi line text
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# number_input() - merupakan widget untuk memperoleh inputan berupa angka dari pengguna
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), 'tahun')

# date_input() - untuk inputan berupa tanggal
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1990, 1, 1))
st.write('Tanggal lahir:', date)

# file_uloader() - widget ini memungkinkan kita untuk mengupload sebuah berkas tertentu ke dalam webb app
uploaded_file = st.file_uploader('Choose a CSV file')

if uploaded_file: 
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# camera_input() - digunakan untuk meminta user mengambl gambar melalui webcam sekaligus mengunggahnya. 
picture = st.camera_input('Take a Picture')
if picture: 
    st.image(picture)

# button()
if st.button('Say hello'): 
    st.write('Hello there')

# checkbox()
agree = st.checkbox('I agree')

if agree: 
    st.write('Welcome to MyApp')

# radio() - memungkinkan mpengguna untuk memilih satu dari beberapa pilihan yang ada
genre = st.radio(
    label="What your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

if genre:
    st.write(f"Ohh i see, your favorite movie genre is {genre}")

# selectbox() - memungkinakn untk memilih salah satu dari beberapa pilihan yang ada. ia merupakan opsi alternatif dari radio button
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# multiselect() - digunakan agar user dapat memilih leboh dari satu pilihan dari sekumpmulan pilihan yang ada
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# slider() - memungkinkan pengguna untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)