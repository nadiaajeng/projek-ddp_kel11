import streamlit as st
import random
import pandas as pd 

# TAMPILAN CSS DARK NEON 
st.markdown(
    """
    <style>
        /* ===== WARNA UTAMA ===== */
        :root {
            --utama: #9D4EDD;      /* Ungu Neon */
            --gelap1: #0A0014;
            --gelap2: #150026;
            --teks: #EDE7F6;
        }

        /* ===== BACKGROUND UTAMA ===== */
        .stApp {
            background: radial-gradient(circle at top, var(--gelap2), var(--gelap1));
            color: var(--teks);
        }

        /* ===== SIDEBAR ===== */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, var(--gelap2), var(--gelap1));
            box-shadow: 0 0 25px var(--utama);
        }
        [data-testid="stSidebar"] * {
            color: var(--utama) !important;
            font-weight: bold;
        }

        /* ===== HEADER ===== */
        [data-testid="stHeader"] {
            background: linear-gradient(90deg, var(--utama), var(--utama));
            box-shadow: 0 0 20px var(--utama);
        }

        /* ===== JUDUL ===== */
        h1, h2, h3, h4, h5, h6,
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
        .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
            color: var(--teks) !important;
            text-shadow:
                0 0 5px var(--utama),
                0 0 10px var(--utama),
                0 0 20px var(--utama);
            letter-spacing: 1.5px;
        }

        /* ===== TEKS ===== */
        p, li, span, label {
            color: var(--teks) !important;
            font-size: 16px;
        }
        /* ===== AREA UPLOAD FOTO ===== */
        [data-testid="stFileUploaderDropzone"] {
           background-color: var(--gelap1) !important;
           border: 2px dashed var(--utama) !important;
           color: var(--teks) !important;
           box-shadow: 0 0 10px var(--utama);
           border-radius: 12px;
           padding: 20px;
        }

       /* ===== TOMBOL BROWSE FILES ===== */
        button[data-testid="stFileUploaderBrowseButton"] {
           background-color: var(--utama) !important;
           color: black !important;
           font-weight: bold !important;
           border-radius: 10px !important;
           box-shadow: 0 0 10px var(--utama);
        }

        /* ===== LABEL UPLOAD FOTO ===== */
        [data-testid="stFileUploaderLabel"] {
           color: var(--teks) !important;
           font-size: 16px;
           font-weight: bold;
        }

        /* ===== INPUT ===== */
        input, textarea {
            background-color: var(--gelap1) !important;
            color: var(--teks) !important;
            border: 2px solid var(--utama) !important;
            border-radius: 8px !important;
        }

        /* ===== TOMBOL ===== */
        button {
            background: var(--utama) !important;
            color: black !important;
            border-radius: 12px !important;
            font-weight: bold !important;
            box-shadow: 0 0 15px var(--utama);
        }

        /* ===== RADIO ===== */
        .stRadio label {
            color: var(--utama) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# FUNCTION
def tampilkan_visi_misi(nama):
    if nama in visi_misi:
        st.write("**Visi:**")
        st.write(visi_misi[nama]["visi"])
        st.write("**Misi:**")
        st.write(visi_misi[nama]["misi"])


def tampilkan_profil_kandidat(nama, ukuran_foto=150):
    if nama in foto_calon:
        st.image(foto_calon[nama], width=ukuran_foto)
    tampilkan_visi_misi(nama)

# SESSION STATE
if "calon" not in st.session_state:
    st.session_state.calon = {}
if "foto_calon" not in st.session_state:
    st.session_state.foto_calon = {}
if "visi_misi" not in st.session_state:
    st.session_state.visi_misi = {}

calon = st.session_state.calon
foto_calon = st.session_state.foto_calon
visi_misi = st.session_state.visi_misi


# SIDEBAR (5 HALAMAN)
st.sidebar.title("⚡ MENU KITA ⚡")
menu = st.sidebar.radio(
    "Navigasi",
    [
        "Beranda",
        "Daftar Calon",
        "Voting",
        "Hasil Pemilihan",
        "Tentang Aplikasi",
        "Kontak Pencipta"
    ]
)


# BERANDA
if menu == "Beranda":
    st.image("https://faperta.umsb.ac.id/upload/organisasi.jpg", width=750)
    st.title("Pemilihan Ketua ORGANISASI")

    st.write("""
    Aplikasi **Pemilihan Ketua Organisasi** dengan
    **tema Dark Neon futuristik**.

    **Fitur Utama:**
    - Input kandidat
    - Foto + visi misi
    - Voting online
    - Perhitungan suara otomatis
    - Grafik hasil pemilihan

    ---

    ### 🔥 Kenapa Aplikasi Ini Unik?
    Dibuat dengan desain modern dan interaktif, aplikasi ini memberikan pengalaman pemilihan yang:
    - Transparan dan real-time
    - Mudah digunakan oleh semua kalangan
    - Menarik secara visual dengan tema neon yang futuristik

    ---

    ### 🧠 Siapa yang Cocok Menggunakan?
    - Organisasi sekolah dan kampus
    - Komunitas atau klub
    - Simulasi pembelajaran demokrasi
    - Event pemilihan internal

    ---

    ### 🎨 Desain & Branding
    Tema **Dark Neon** dipilih untuk memberikan kesan:
    - Elegan dan profesional
    - Modern dan digital
    - Berbeda dari aplikasi pemilihan biasa

    ---

    ### 📢 Yuk Mulai!
    Gunakan menu di samping untuk:
    - Menambahkan kandidat
    - Melakukan voting
    - Melihat hasil pemilihan
    - Mengenal aplikasi lebih dalam

    """)

# DAFTAR CALON
elif menu == "Daftar Calon":
    st.title("Input Nama Kandidat")

    nama = st.text_input("Nama Kandidat")
    kelas = st.text_input("Kelas Kandidat")
    foto = st.file_uploader("Upload Foto Kandidat", type=["jpg", "jpeg", "png"])
    visi = st.text_area("Visi Kandidat")
    misi = st.text_area("Misi Kandidat")

    if st.button("➕ Tambah Kandidat"):
        if nama and kelas:
            nama_final = f"{nama} ({kelas})"
            if nama_final not in calon:
                calon[nama_final] = 0
                if foto:
                    foto_calon[nama_final] = foto
                visi_misi[nama_final] = {"visi": visi, "misi": misi}
                st.success("Kandidat berhasil ditambahkan")
            else:
                st.warning("Kandidat sudah ada")
        else:
            st.error("Nama dan kelas wajib diisi")

    st.subheader("📋 Daftar Kandidat")
    if calon:
        for c in calon:
            st.write(f"### {c}")
            tampilkan_profil_kandidat(c)
            st.write("---")
    else:
        st.warning("Belum ada kandidat")


# VOTING
elif menu == "Voting":
    st.title("Voting Ketua ORGANISASI")

    if calon:
        pilihan = st.radio("Pilih Kandidat", list(calon.keys()))
        tampilkan_profil_kandidat(pilihan, 200)

        if st.button("🗳️ Kirim Suara"):
            calon[pilihan] += 1
            st.success("Suara berhasil direkam")
    else:
        st.warning("Belum ada kandidat")


# HASIL PEMILIHAN
elif menu == "Hasil Pemilihan":
    st.title("Hasil Pemilihan")

    if calon:
        for nama, suara in calon.items():
            st.write(f"## {nama}")
            tampilkan_profil_kandidat(nama)
            st.write(f"**{suara} suara**")
            st.write("---")

        st.subheader("📊 Grafik Perolehan Suara")
        st.bar_chart(calon)
    else:
        st.warning("Belum ada hasil")


# TENTANG APLIKASI
elif menu == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")

    st.write("""
    Aplikasi ini dibuat sebagai **media pembelajaran** dan simulasi **Pemilihan Ketua Organisasi**.

    Menggunakan:
    - Python
    - Streamlit
    - Konsep CRUD & Voting
    - UI Dark Neon Futuristik

    ---

    ### 🎯 Tujuan Pengembangan
    Aplikasi ini dirancang untuk memberikan pengalaman interaktif dalam proses pemilihan ketua organisasi.  
    Pengguna dapat:
    - Menambahkan kandidat beserta foto, visi, dan misi  
    - Melakukan voting secara langsung  
    - Melihat hasil perolehan suara secara real-time  
    - Menampilkan grafik visual untuk analisis hasil pemilihan  

    ---

    ### 🛠️ Teknologi yang Digunakan
    Aplikasi ini memanfaatkan:
    - **Streamlit** untuk tampilan antarmuka yang cepat dan responsif  
    - **Python** sebagai bahasa pemrograman utama  
    - **Session State** untuk menyimpan data kandidat dan suara  
    - **Custom CSS** bertema *Dark Neon* untuk tampilan modern dan futuristik  

    ---

    ### 🚀 Keunggulan Aplikasi
    - Tampilan elegan dan modern  
    - Mudah digunakan oleh siapa saja  
    - Tidak memerlukan database eksternal  
    - Cocok untuk simulasi kelas, organisasi sekolah, kampus, atau komunitas  

    ---

    ### 👨‍💻 Pengembang
    Aplikasi ini dikembangkan sebagai bagian dari latihan pemrograman dan pembuatan aplikasi berbasis web menggunakan Streamlit.
    """)
    
# ================== KONTAK PENCIPTA ==================
elif menu == "Kontak Pencipta":
    st.title("📞 Kontak Pencipta")
    st.write("Klik tombol di bawah untuk langsung terhubung ke WhatsApp atau Instagram pencipta aplikasi berikan masukan mu jika website ini masih banyak kesalahan")

    # Logo WA dan IG
    logo_wa = "logo_wa.png"   
    logo_ig = "logo_ig.jpg"   

    # Tambahkan foto profil tiap pencipta
    kontak = [
        {"nama": "Irfan Mardiansyah", "wa": "+62 889-7623-9985", "ig": "@skyfanza18", "foto": "foto1.jpeg"},
        {"nama": "Azra Pramadany Hasibuan", "wa": "+62 882-2415-4129", "ig": "@azra_hsb", "foto": "foto2.jpeg"},
        {"nama": "Nadia Ajeng Salsabila Saffa", "wa": "+62 896-5371-3432", "ig": "@nadiaajengg", "foto": "foto3.jpg"},
        {"nama": "Mahmudin", "wa": "+62 822-5281-3095", "ig": "@mahmudinn_ritongaa", "foto": "foto4.jpeg"},
    ]

    for k in kontak:
        st.markdown(f"<h3 style='color:#9D4EDD;'>{k['nama']}</h3>", unsafe_allow_html=True)

        # Layout: Foto profil di kiri, tombol di kanan
        col1, col2 = st.columns([1,2])

        with col1:
            st.image(k["foto"], width=150)

        with col2:
            # Tombol WhatsApp
            st.link_button(
                "💬 Chat WhatsApp",
                url=f"https://wa.me/{k['wa'].replace('+','').replace(' ','').replace('-','')}",
                type="primary"
            )
            # Tombol Instagram
            st.link_button(
                "📸 Kunjungi Instagram",
                url=f"https://instagram.com/{k['ig'].replace('@','')}",
                type="secondary"
            )

        st.write("---")