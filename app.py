import streamlit as st
from werkzeug.security import generate_password_hash

# Konfigurasi Tampilan
st.set_page_config(page_title="PLN - Password Hasher", page_icon="⚡")

st.title("Password Hasher")
st.subheader("Membuat Hash Password")
st.info("Tools ini menghasilkan hash untuk kolom 'password_hash' di BigQuery tanpa database.")

# Input Password
password_asli = st.text_input("Masukkan Password Asli:", placeholder=" ")

if password_asli:
    # Generate Hash
    hash_code = generate_password_hash(password_asli, method='pbkdf2:sha256')
    
    st.write("---")
    st.success("Berhasil Generate!")
    
    # Menampilkan hasil dalam box kode agar mudah di-copy
    st.code(hash_code, language='text')
    
    st.warning("Copy 'Hash Code' di atas dan ikuti dokumentasi")
    
    # Tambahan: Detail format
    with st.expander("Lihat Detail Format"):
        st.write(f"Method: pbkdf2:sha256")
        st.write(f"Karakter: {len(hash_code)}")
