import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# PAGE CONFIG

st.set_page_config(
    page_title="Dashboard Analisis Penjualan",
    page_icon="📊",
    layout="wide"
)

# SIDEBAR – IDENTITAS & NAVIGASI

st.sidebar.title("👤 Profil Pembuat")
st.sidebar.write("**Nama:** Amirullah Adi Setya Wicaksana")
st.sidebar.write("**NIM:** 4232401016")
st.sidebar.write("**Program Studi:** Teknologi Rekayasa Pembangkit Energi")
st.sidebar.write("**Mata Kuliah:** Pemrograman Dasar")

st.sidebar.divider()

st.sidebar.title("📌 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["Pendahuluan", "Ringkasan Kinerja", "Data & Grafik", "Profil Pembuat", "Kesimpulan"]
)

st.sidebar.caption("Dashboard dibuat menggunakan Streamlit")


# DATA

data = {
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni"],
    "Penjualan": [120, 150, 170, 160, 190, 220],
    "Keuntungan": [30, 45, 50, 48, 60, 75]
}
df = pd.DataFrame(data)


# HEADER UTAMA

st.title("📊 Dashboard Analisis Penjualan Bulanan")
st.caption(
    "Dashboard interaktif untuk menganalisis performa penjualan "
    "berdasarkan data dan visualisasi."
)

st.divider()


# PENDAHULUAN

if menu == "Pendahuluan":
    st.header("📘 Pendahuluan")
    st.write(
        "Analisis data penjualan merupakan bagian penting dalam "
        "mengevaluasi kinerja suatu usaha. Dengan menyajikan data "
        "dalam bentuk visual, proses analisis menjadi lebih mudah "
        "dipahami dan informatif."
    )

    with st.expander("🎯 Tujuan Dashboard"):
        st.write(
            "Dashboard ini bertujuan untuk menyajikan data penjualan "
            "secara ringkas, membantu memahami tren penjualan, serta "
            "mendukung pengambilan keputusan berbasis data."
        )

# RINGKASAN KINERJA

elif menu == "Ringkasan Kinerja":
    st.header("📌 Ringkasan Kinerja Penjualan")

    col1, col2, col3 = st.columns(3)

    col1.metric("📦 Total Penjualan", f"{df['Penjualan'].sum()} Unit")
    col2.metric("💰 Total Keuntungan", f"{df['Keuntungan'].sum()} Unit")
    col3.metric("📈 Rata-rata Penjualan", f"{round(df['Penjualan'].mean(), 1)} Unit")

    st.success(
        "📈 **Insight:** Penjualan tertinggi terjadi pada bulan Juni, "
        "menunjukkan peningkatan performa di akhir periode."
    )


# DATA & GRAFIK

elif menu == "Data & Grafik":
    st.header("📊 Data Penjualan dan Visualisasi")

    left, right = st.columns([1, 2])

    with left:
        st.subheader("📋 Tabel Data Penjualan")
        st.dataframe(df, use_container_width=True)

        with st.expander("🧠 Interpretasi Data"):
            st.write(
                "Data menunjukkan tren peningkatan penjualan dari bulan "
                "ke bulan. Meskipun terdapat sedikit penurunan pada bulan April, "
                "kondisi tersebut tidak memengaruhi tren keseluruhan."
            )

    with right:
        st.subheader("📈 Grafik Tren Penjualan & Keuntungan")

        fig, ax = plt.subplots()
        ax.plot(df["Bulan"], df["Penjualan"], marker="o", label="Penjualan")
        ax.plot(df["Bulan"], df["Keuntungan"], marker="o", label="Keuntungan")
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Jumlah")
        ax.set_title("Tren Penjualan dan Keuntungan Bulanan")
        ax.legend()

        st.pyplot(fig)

        st.subheader("📊 Grafik Perbandingan Penjualan")
        st.bar_chart(df.set_index("Bulan")[["Penjualan"]])


# PROFIL PEMBUAT

elif menu == "Profil Pembuat":
    st.header("👤 Profil Pembuat Dashboard")

    st.write(
        "Dashboard ini dibuat sebagai bagian dari tugas akademik "
        "untuk menerapkan konsep analisis data dan visualisasi "
        "menggunakan Streamlit."
    )

    st.markdown(
        """
        **Identitas Pembuat:**
        - **Nama:** Amirullah Adi Setya Wicaksana  
        - **NIM:** 4232401016  
        - **Program Studi:** Teknologi Rekayasa Pembangkit Energi
        - **Mata Kuliah:** Pemrograman Dasar
        - **Institusi:** Politeknik Negeri Batam
        """
    )

    st.info(
        "📌 Dashboard ini diharapkan dapat membantu pemahaman "
        "mengenai analisis data penjualan secara visual dan interaktif."
    )


# KESIMPULAN

elif menu == "Kesimpulan":
    st.header("✅ Kesimpulan")
    st.write(
        "Berdasarkan analisis yang dilakukan, dapat disimpulkan "
        "bahwa penjualan menunjukkan tren peningkatan secara "
        "keseluruhan. Dashboard ini membuktikan bahwa Streamlit "
        "merupakan alat yang efektif untuk menyajikan analisis data "
        "secara ringkas dan mudah dipahami."
    )


# FOOTER

st.divider()
st.caption(
    "Dashboard Analisis Penjualan | "
    "Dibuat oleh Amirullah Adi Setya Wicaksana menggunakan Streamlit"
)
