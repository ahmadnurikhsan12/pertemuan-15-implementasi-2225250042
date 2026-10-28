# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Identitas Mahasiswa

- **Nama:** Ahmad Nurikhsan
- **NIM:** 2225250042
- **Kelas:** 3E
- **Program Studi:** Pendidikan Matematika
- **Fakultas:** FKIP
- **Universitas:** Universitas Sultan Ageng Tirtayasa

## 2. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program sederhana berbasis Python yang digunakan untuk membaca data nilai siswa, menghitung statistik nilai, dan menampilkan ringkasan kelulusan berdasarkan batas nilai yang telah ditentukan.

## 3. Fitur Program

- Membaca data nama dan nilai siswa dari file teks.
- Memvalidasi format data dan rentang nilai siswa.
- Menghitung rata-rata nilai siswa.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah siswa yang lulus dan belum lulus.
- Menampilkan hasil analisis melalui terminal.

## 4. Persyaratan

- Python 3.
- Visual Studio Code sebagai editor yang disarankan.

## 5. Cara Menjalankan Program

1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Pastikan file data tersedia di `data/contoh_data.txt`.
4. Jalankan perintah berikut pada terminal:

   ```bash
   python main.py
   ```

5. Hasil rekap dan analisis nilai akan ditampilkan di terminal.

Batas kelulusan yang digunakan dalam program ini adalah nilai 60.

## 6. Struktur Folder

```text
pertemuan-15-implementasi-2225250042/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/
```

## 7. Pengujian Program

Pengujian direncanakan mencakup beberapa kondisi berikut:

1. Data nilai normal.
2. Nilai tepat pada batas kelulusan.
3. Nilai yang bukan berupa angka.
4. Nilai di luar rentang 0–100.
5. File data tidak ditemukan.
6. File data kosong atau tidak memiliki data valid.

Rincian kasus uji, hasil yang diharapkan, hasil aktual, dan status pengujian dicatat dalam file `tests/test_case.md`. Hasil aktual dan status akan diperbarui setelah pengujian dilakukan.

## 8. Batasan yang Diketahui

- Data siswa menggunakan format `nama,nilai`.
- Nilai yang diterima berada pada rentang 0 sampai 100.
- Program membaca data dari file teks lokal.
- Program belum menggunakan database atau antarmuka grafis.

## 9. Kontribusi

Ahmad Nurikhsan bertanggung jawab atas pengembangan program, pengujian, dan penyusunan dokumentasi proyek.

## 10. Referensi dan Bantuan

- Modul Algoritma dan Pemrograman Pertemuan 15: *Implementasi, Pengujian, dan Dokumentasi Proyek Python di VS Code, Git, dan GitHub*.
- Dokumentasi resmi Python: https://docs.python.org/3/
- Bantuan AI digunakan untuk membantu penyusunan dan peninjauan kode serta dokumentasi. Implementasi dan hasil pengujian tetap diperiksa oleh mahasiswa.