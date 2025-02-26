import streamlit as st

# Sidebar - merupakan area yang berada di samping kotent utama. secara default berada di sisi kiri dari kontent utama dan dapat memuat berbagai hal mulai dari gambar teks hingga widgets.

st.title('Belajar Analisis Data')

with st.sidebar:
    
    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)

# Columns - merupakan elemen laytou yang memungkinkna kita untuk mengatur tampilan pada konten utama ke dalam beberapa kolom sesuai kebutuhan.

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")