# Movie-Sentimen-Analyze_DataMining_SubProject

Proyek ini adalah aplikasi analisis sentimen ulasan film yang dikembangkan untuk mendeteksi apakah ulasan yang diberikan bersifat **positif** atau **negatif**. Proyek ini menggunakan **Support Vector Machine (SVM)** sebagai model klasifikasi, yang dilatih menggunakan dataset ulasan film dari IMDb.

---

## **Fitur Utama**
1. **Analisis Sentimen**:
   - Mengklasifikasikan ulasan film menjadi **positif** atau **negatif**.
   - Mendukung input teks ulasan yang panjang.

2. **Preprocessing Teks**:
   - Membersihkan data teks untuk meningkatkan akurasi.
   - Menggunakan **TfidfVectorizer** untuk mengubah teks menjadi fitur numerik.

3. **Antarmuka Sederhana**:
   - Aplikasi berbasis web yang dibuat menggunakan **Streamlit**.
   - Pengguna hanya perlu memasukkan ulasan dan hasil analisis akan langsung ditampilkan.

4. **Model yang Optimal**:
   - Model dilatih menggunakan **GridSearchCV** untuk optimasi hyperparameter.
   - Akurasi pada data uji mencapai **~85%**.

---

## **Teknologi yang Digunakan**
1. **Python**: Bahasa pemrograman utama.
2. **Library Utama**:
   - **scikit-learn**: Untuk pembuatan dan evaluasi model machine learning.
   - **nltk**: Untuk pengelolaan dataset dan preprocessing teks.
   - **Streamlit**: Untuk membangun antarmuka aplikasi web.
3. **Framework untuk Deploy**:
   - **Streamlit Community Cloud**.

---

## **Cara Menjalankan Proyek**
1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/Movie-Sentimen-Analyze_DataMining_SubProject.git
   cd Movie-Sentimen-Analyze_DataMining_SubProject
   ```

2. **Instalasi Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**:
   ```bash
   streamlit run app.py
   ```

4. **Akses Aplikasi**:
   - Aplikasi akan terbuka secara otomatis di browser Anda.
   - Masukkan teks ulasan pada kolom yang tersedia untuk mendapatkan hasil analisis.

---

## **Contoh Penggunaan**
### **Input**:
```
Film ini sangat membosankan, tidak ada alur cerita yang jelas dan aktingnya buruk.
```
### **Output**:
```
Hasil Sentimen: Negatif
```

### **Input**:
```
Film ini luar biasa! Alur ceritanya menyentuh dan aktingnya sempurna.
```
### **Output**:
```
Hasil Sentimen: Positif
```

---

## **Catatan Penting**
1. Aplikasi ini saat ini lebih optimal untuk ulasan dalam **bahasa Inggris**. Untuk bahasa Indonesia, disarankan melatih ulang model menggunakan dataset ulasan berbahasa Indonesia.
2. Dataset yang digunakan adalah dataset ulasan IMDb bawaan dari **nltk**.

---

## **Pengembangan Lebih Lanjut**
Beberapa fitur yang dapat ditambahkan:
- **Dukungan untuk Bahasa Indonesia**:
  - Gunakan dataset lokal untuk melatih ulang model.
- **Visualisasi Data**:
  - Tambahkan grafik untuk memperlihatkan distribusi ulasan atau akurasi model.
- **Deploy ke Cloud**:
  - Akses aplikasi secara publik melalui layanan seperti **Streamlit Cloud** atau **Heroku**.

---

## **Kontributor**
- Nama Anda
- Proyek ini dikembangkan untuk keperluan **UAS Data Mining**.

---

## **Lisensi**
Proyek ini menggunakan lisensi [MIT License](LICENSE).

---

Jika ada bagian yang perlu disesuaikan, beri tahu saya!
