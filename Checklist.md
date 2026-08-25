# FORMAT ID

`Hari.Role.Checkpoint+Nomor` → contoh `2.1.A2` = Hari 2, Role 1, checkpoint A (19.00), task 2

- Checkpoint: **P** = Persiapan, **A** = 19.00, **B** = 20.00, **C** = 21.30, **X** = Cross Check
- Role: 1–4, **S** = Semua Role
- **Bold + (→ dipakai di ...)** = output task ini ditunggu role lain, PRIORITASKAN
- **(tunggu ...)** = jangan mulai sebelum ID tersebut selesai

---

# PEMBAGIAN ROLE

- Role 1 — Data Engineer & Airflow Pipeline
- Role 2 — Database & Data Modeling
- Role 3 — Data Analyst
- Role 4 — BI, Documentation & Presentation

---

# HARI 1 — Kunci Masalah & Data

## Persiapan — Semua Role

- [x]  `1.S.P1` Repo siap, semua bisa push
- [x]  `1.S.P2` Sepakati tools, struktur folder, role, output akhir

## 19.00 — Tentukan Masalah

### Role 1

- [x]  **`1.1.A1` Cari & finalkan dataset, pastikan bisa dibuka Python** **(tunggu 1.3.A1)** **(→ dipakai di 1.2.A1, 1.3.B1)**
- [x]  `1.1.A2` Cek format, jumlah baris/kolom
- [x]  `1.1.A3` Simpan raw data tanpa perubahan

### Role 2

- [x]  `1.2.A1` Pelajari struktur dataset **(tunggu 1.1.A1)**
- [x]  `1.2.A2` Identifikasi primary key & relasi

### Role 3

- [x]  **`1.3.A1` Pilih 1 SDG + 1 masalah spesifik** **(→ dipakai di 1.1.A1, 1.4.A1)**
- [x]  **`1.3.A2` Tentukan stakeholder + KPI utama** **(→ dipakai di 1.4.A1)**
- [x]  `1.3.A3` Susun 3–5 pertanyaan analisis

Format: Kami membantu [stakeholder] mengambil keputusan [X] dengan menganalisis [data], agar [metrik] naik/turun dari [baseline] ke [target].

### Role 4

- [x]  `1.4.A1` Struktur awal README (problem, SDG, stakeholder, dataset, role) **(tunggu 1.3.A1, 1.3.A2)**
- [ ]  `1.4.A2` Siapkan folder dokumentasi & screenshot

## 20.00 — Pahami Data

### Role 1

- [ ]  `1.1.B1` Cek missing, duplicate, tipe data, nilai aneh
- [ ]  **`1.1.B2` Tentukan proses cleaning, transformasi, validation rule** **(→ dipakai di 1.2.C1)**

### Role 2

- [x]  `1.2.B1` Rancang schema: tabel, tipe data, key, constraint
- [x]  `1.2.B2` Tentukan tabel/view untuk analyst & dashboard

### Role 3

- [ ]  **`1.3.B1` Buat data dictionary** **(tunggu 1.1.A1)** **(→ dipakai di 1.4.B1)**
- [ ]  `1.3.B2` Tentukan rumus KPI & baseline

### Role 4

- [ ]  `1.4.B1` Rapikan data dictionary ke README **(tunggu 1.3.B1)**
- [ ]  `1.4.B2` Outline slide & struktur dashboard

## 21.30 — Bersihkan & Rancang

### Role 1

- [ ]  `1.1.C1` Script cleaning + transformasi + validation awal (via kode)
- [ ]  `1.1.C2` Tentukan struktur DAG: `Source → Extract → Transform → Validate → Load → DB`
- [ ]  `1.1.C3` Push kode awal

### Role 2

- [x]  **`1.2.C1` Finalisasi rancangan DB + mulai `schema.sql`** **(tunggu 1.1.B2)** **(→ dipakai di 2.2.A1)**

### Role 3

- [ ]  `1.3.C1` EDA awal, minimal 3 temuan
- [ ]  `1.3.C2` Hitung baseline KPI jika bisa

### Role 4

- [ ]  `1.4.C1` Buat diagram arsitektur
- [ ]  `1.4.C2` Update README & dokumentasikan temuan awal

## TARGET AKHIR HARI 1

- [ ]  Masalah, SDG, stakeholder, dataset, KPI, pertanyaan analisis final
- [ ]  Data dictionary selesai, cleaning awal jalan
- [ ]  Rancangan database & DAG selesai
- [ ]  README awal tersedia, semua di-push

---

# HARI 2 — Pipeline, Database, Analisis & Dashboard

Rantai kritis: `2.2.A1 → 2.2.A2 → 2.1.A2 → 2.2.A3 → 2.3.A2 → 2.4.C1`

## 19.00 — Pipeline & Database Jalan

### Role 1

- [ ]  `2.1.A1` Buat `extract.py`, `transform.py`, `validate.py`, `load.py` + DAG (bisa mulai tanpa menunggu)
- [ ]  **`2.1.A2` Tes DAG penuh sampai load sukses ke DB + screenshot** **(tunggu 2.2.A1, 2.2.A2)** **(→ dipakai di 2.2.A3, 2.4.A1)**
- [ ]  `2.1.A3` Credential di `.env`/Airflow Connection, bukan di kode

### Role 2

- [ ]  **`2.2.A1` Setup PostgreSQL/Neon + jalankan `schema.sql` (buat tabel)** **(tunggu 1.2.C1)** **(→ dipakai di 2.1.A2)** ⚠️ BLOCKER TERBESAR, kerjakan pertama
- [ ]  **`2.2.A2` Beri info koneksi ke Role 1 dengan aman** **(→ dipakai di 2.1.A2)**
- [ ]  **`2.2.A3` Validasi hasil load: row count, PK, duplicate, null** **(tunggu 2.1.A2)** **(→ dipakai di 2.3.A2)**

### Role 3

- [ ]  `2.3.A1` Siapkan semua SQL query analisis duluan (paralel, tanpa menunggu)
- [ ]  `2.3.A2` Ambil data dari database + mulai hitung KPI **(tunggu 2.2.A3)** — jangan pakai raw CSV

### Role 4

- [ ]  `2.4.A1` Dokumentasi pipeline + screenshot DAG **(tunggu 2.1.A2)**
- [ ]  `2.4.A2` Setup tool dashboard & layout dengan data sampel (paralel)

## 20.00 — Jawab Pertanyaan Analisis

### Role 1

- [ ]  `2.1.B1` Fix error Airflow, pastikan rerun tidak duplicate

### Role 2

- [ ]  **`2.2.B1` Buat view/query siap pakai untuk Role 3 & 4** **(→ dipakai di 2.4.C1)**

### Role 3

- [ ]  **`2.3.B1` Jawab 3–5 pertanyaan, hasilkan 3 insight + 3 rekomendasi** **(→ dipakai di 2.4.B1)**

Format: | Pertanyaan | Bukti/Data | Insight | Tindakan |

### Role 4

- [ ]  `2.4.B1` Tentukan KPI & 3–6 grafik dashboard **(tunggu 2.3.B1)**
- [ ]  `2.4.B2` Mulai buat dashboard

## 21.30 — Dashboard V1

### Role 1

- [ ]  `2.1.C1` Rerun DAG, semua task sukses + screenshot final

### Role 2

- [ ]  `2.2.C1` Pastikan DB & query siap untuk dashboard

### Role 3

- [ ]  `2.3.C1` Validasi angka: `Database = Notebook = Dashboard` **(tunggu 2.4.C1)**
- [ ]  `2.3.C2` Narasi singkat 3 insight utama

### Role 4

- [ ]  **`2.4.C1` Dashboard 1 halaman: KPI, 3–6 grafik, filter, label jelas** **(tunggu 2.2.B1, 2.4.B1)** **(→ dipakai di 2.3.C1)**
- [ ]  `2.4.C2` Tes public link + screenshot + update README

## TARGET AKHIR HARI 2

- [ ]  DAG jalan end-to-end, data masuk & tervalidasi di DB
- [ ]  Tidak ada credential di Git
- [ ]  3 insight + 3 rekomendasi tersedia
- [ ]  Dashboard v1 selesai

---

# HARI 3 — Final QA, Dokumentasi, Slide & Presentasi

Rantai kritis: `3.2.A1 → 3.1.A1 → 3.2.A2 → 3.3.A1 → 3.3.A2 → 3.4.B1 → 3.S.C1`

## 19.00 — Tes Ulang & Rapikan Repo

### Role 1

- [ ]  **`3.1.A1` Jalankan pipeline dari nol tanpa edit manual** **(tunggu 3.2.A1)** **(→ dipakai di 3.2.A2, 3.3.A1)**
- [ ]  `3.1.A2` Tes validation gagal & rerun tanpa duplicate
- [ ]  `3.1.A3` Finalisasi `requirements.txt` & `.env.example`

### Role 2

- [ ]  **`3.2.A1` Tes `schema.sql` dari awal** **(→ dipakai di 3.1.A1)**
- [ ]  **`3.2.A2` Cek database menyeluruh** **(tunggu 3.1.A1)** **(→ dipakai di 3.3.A1)**

### Role 3

- [ ]  `3.3.A1` Rerun analisis dari awal, data dari DB **(tunggu 3.1.A1, 3.2.A2)**
- [ ]  **`3.3.A2` Finalisasi KPI, 3 insight, 3 rekomendasi** **(→ dipakai di 3.4.A1, 3.4.B1)**

### Role 4

- [ ]  `3.4.A1` Finalisasi dashboard & README lengkap **(tunggu 3.3.A2)**

## FINAL CROSS CHECK — Semua Role

Pastikan: `Pipeline = Database = Analysis = Dashboard = README = Slide`

- [ ]  `3.S.X1` Semua angka konsisten
- [ ]  `3.S.X2` Tidak ada credential di Git, `.env` di `.gitignore`, ada `.env.example` & `requirements.txt`
- [ ]  `3.S.X3` Semua link jalan, anggota lain bisa menjalankan pipeline

## 20.00 — Slide Final

### Role 1

- [ ]  `3.1.B1` Siapkan penjelasan: pipeline, DAG, alasan pakai Airflow

### Role 2

- [ ]  `3.2.B1` Siapkan penjelasan: database, schema, data model, validation

### Role 3

- [ ]  `3.3.B1` Siapkan penjelasan: KPI, baseline, insight, rekomendasi, impact

### Role 4

- [ ]  **`3.4.B1` Susun slide final (angka dari hasil final)** **(tunggu 3.3.A2)** **(→ dipakai di 3.S.C1)**

Aturan: 1 slide = 1 pesan, teks singkat, angka sama dengan dashboard, cantumkan sumber dataset.

## 21.30 — Latihan & Submit

### Semua Role

- [ ]  `3.S.C1` Latihan presentasi 2x, target 7–8 menit **(tunggu 3.4.B1)**
- [ ]  `3.S.C2` Latihan buka dashboard, repo, jelaskan DAG, jawab Q&A

### Role 1

- [ ]  `3.1.C1` Tes Airflow terakhir + push kode final

### Role 2

- [ ]  `3.2.C1` Tes database terakhir + cek credential aman

### Role 3

- [ ]  `3.3.C1` Cek angka, insight, rekomendasi terakhir

### Role 4

- [ ]  `3.4.C1` Cek dashboard, README, link + export slide PDF

---

# ALOKASI PRESENTASI 7–8 MENIT

| Bagian | Waktu | PIC |
| --- | --- | --- |
| Intro + masalah | 45 dtk | Role 4 |
| Objective + KPI | 45 dtk | Role 3 |
| Pipeline | 60 dtk | Role 1 |
| Database | 45 dtk | Role 2 |
| Dashboard + 3 insight | 2,5–3 mnt | Role 3 & 4 |
| Rekomendasi + impact | 1–1,5 mnt | Role 3 |
| Conclusion | 45 dtk | Role 4 |

---

# ATURAN PENYELAMAT

| Kondisi | Yang Dilakukan |
| --- | --- |
| MERAH di 19.00 | Buang fitur opsional |
| MERAH di 20.00 | Pakai cara paling sederhana |
| Lewat 21.30 | Stop fitur baru |
| Airflow bermasalah | DAG sederhana yang jalan end-to-end |
| Database bermasalah | Schema paling sederhana yang benar |
| Dashboard belum selesai | Kurangi grafik, jangan kurangi insight |
| Analisis terlalu luas | Kembali ke 3 pertanyaan penting |
| Slide terlalu panjang | Buang detail teknis ke Q&A |

# PRIORITAS JIKA MEPET

1. Problem + KPI
2. Pipeline + load ke database
3. 3 insight + 3 rekomendasi
4. Dashboard 1 halaman
5. README + slide + latihan

> Proyek sederhana yang berjalan end-to-end lebih kuat daripada proyek kompleks yang tidak selesai.
>
