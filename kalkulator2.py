import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Modern Streamlit", 
    page_icon="🧮", 
    layout="centered"
)

# Header dengan Gambar/Banner
st.image(
    "https://camo.githubusercontent.com/e940f9b6438dcb66f33380af6991175285262e218c217c3800d13374d470e5ef/68747470733a2f2f692e6962622e636f2f374366564e58432f696d6167656d2d323032332d31302d32342d3038353633363735302e706e67" \
    use_container_width=True,
    caption="Smart & Modern Calculator App"
)

st.title("🧮 Kalkulator Advance dengan Streamlit")
st.markdown("Aplikasi kalkulator interaktif yang dilengkapi dengan sistem **Riwayat Perhitungan (History)**.")

# Inisialisasi session state untuk menyimpan riwayat perhitungan
if 'history' not in st.session_state:
    st.session_state.history = []

# Layout menggunakan kolom (2 kolom sejajar)
col1, col2 = st.columns(2)

with col1:
    angka1 = st.number_input("Masukkan angka pertama", value=0.0, format="%.2f")

with col2:
    angka2 = st.number_input("Masukkan angka kedua", value=0.0, format="%.2f")

# Pilihan operasi matematika
operasi = st.selectbox(
    "Pilih operasi matematika:",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)", "Pangkat (^)")
)

# Tombol aksi
col_btn1, col_btn2 = st.columns([1, 1])

with col_btn1:
    hitung = st.button("Hitung Sekarang 🚀", use_container_width=True)

with col_btn2:
    reset_history = st.button("Hapus Riwayat 🗑️", use_container_width=True)

if reset_history:
    st.session_state.history = []
    st.success("Riwayat berhasil dibersihkan!")

# Proses Perhitungan
if hitung:
    hasil = None
    ekspresi = ""
    
    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2
        ekspresi = f"{angka1} + {angka2} = {hasil}"
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
        ekspresi = f"{angka1} - {angka2} = {hasil}"
    elif operasi == "Perkalian (×)":
        hasil = angka1 * angka2
        ekspresi = f"{angka1} × {angka2} = {hasil}"
    elif operasi == "Pembagian (÷)":
        if angka2 != 0:
            hasil = angka1 / angka2
            ekspresi = f"{angka1} ÷ {angka2} = {hasil}"
        else:
        # Tambahan error handling khusus pembagian nol
            st.error("⚠️ Kesalahan: Pembagian dengan nol tidak diperbolehkan!")
    elif operasi == "Pangkat (^)":
        hasil = angka1 ** angka2
        ekspresi = f"{angka1} ^ {angka2} = {hasil}"

    if hasil is not None:
        st.success(f"### Hasil: **{hasil}**")
        # Simpan ke riwayat (paling atas)
        st.session_state.history.insert(0, ekspresi)

# Menampilkan Riwayat Perhitungan (History)
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Riwayat Perhitungan Terakhir")
    for item in st.session_state.history[:5]:  # Tampilkan 5 riwayat terbaru
        st.write(f"- {item}")