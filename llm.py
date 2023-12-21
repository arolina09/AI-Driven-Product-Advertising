# Tambahkan library Font Awesome
import streamlit as st
import google.generativeai as genai

# Konfigurasi GenerativeAI dari Google
genai.configure(api_key="AIzaSyCIwTh67hoG_iQt3PKJhT0_d3Ex21lFLuM")

# Default parameters for text generation
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.85,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
}

# Streamlit app
st.title("AI-Driven Product Advertising")

# Meminta input dari pengguna (merek barang)
brand_input = st.text_input("Masukkan merek barang:")

# Generate text using Google GenerativeAI
if st.button("Search"):
    if brand_input:
        prompt_text = f"Product: {brand_input}\nProduct Copy: "
        response = genai.generate_text(
            **defaults,
            prompt=prompt_text
        )

        # Menampilkan hasil
        st.write("Iklan Produk:")
        st.write(response.result)
    else:
        st.warning("Silakan masukkan merek barang terlebih dahulu.")
