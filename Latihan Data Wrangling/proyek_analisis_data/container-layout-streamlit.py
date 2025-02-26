import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Container - merupakan elemen layout dalam streamlit yang memungkinkan kita untuk membuat sebuah wadah untuk menampung suatu atau beberapa elemen dengan ukuran yang tetap

with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

st.write('Outside the container')