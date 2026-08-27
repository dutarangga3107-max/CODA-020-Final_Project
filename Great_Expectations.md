# Dokumentasi Data Validation — Great Expectations

## Validasi RAW (`validate_raw`, di `FP_extract.py`)

Dijalankan setelah data mentah berhasil di-download dari CTDC, sebelum masuk ke tahap transform.

| Expectation | Alasan |
|---|---|
| `expect_table_columns_to_match_set` | Memastikan struktur kolom CSV yang di-download sama persis dengan yang diharapkan. Kalau sumber data (CTDC) mengubah struktur kolom, pipeline langsung berhenti di sini alih-alih memproses data yang salah. |
| `expect_table_row_count_to_be_between` (min 100.000) | Deteksi dini kalau file yang ter-download rusak/terpotong (misal koneksi putus saat download), yang biasanya menghasilkan file dengan baris jauh lebih sedikit dari seharusnya. |
| `expect_column_values_to_be_in_set` (kolom flag, value `["1"]`) | Kolom flag (mis. `isForcedLabour`, `meansThreats`) di data mentah hanya boleh berisi `"1"` atau kosong (missing = tidak terjadi). Validasi ini memastikan tidak ada nilai tak terduga selain `"1"`. |
| `expect_column_values_to_be_in_set` (kolom `gender`) | Memastikan nilai `gender` hanya berisi kategori yang dikenal (`Man`, `Woman`, `Trans/Transgender/NonConforming`), mendeteksi kalau ada nilai baru/typo dari sumber data. |

## Validasi CLEAN (`validate_clean`, di `FP_transform.py`)

Dijalankan setelah data dibersihkan (`transform()`), sebelum disimpan sebagai `clean.parquet` dan dipecah jadi star schema.

| Expectation | Alasan |
|---|---|
| `expect_table_row_count_to_equal` (= jumlah baris raw) | Tahap transform hanya mengubah nilai (fillna, cast tipe), tidak memfilter baris. Validasi ini memastikan tidak ada baris yang hilang secara tidak sengaja selama proses cleaning. |
| `expect_column_values_to_not_be_null` (kolom flag & kategorikal) | Setelah cleaning, semua nilai kosong seharusnya sudah diisi (`False` untuk flag, `'Unknown'` untuk kategorikal). Validasi ini memastikan proses `fillna` benar-benar berhasil di semua baris. |
| `expect_column_values_to_be_in_set` (kolom `gender`) | Sama seperti di raw, tapi sekarang juga mengizinkan nilai `'Unknown'` (hasil dari `fillna`) selain 3 kategori aslinya. |
| `expect_column_values_to_be_between` (`yearOfRegistration`, 2002–2026) | Memastikan tahun registrasi kasus berada dalam rentang yang masuk akal (dataset CTDC dimulai 2002), mendeteksi data tahun yang salah/corrupt. |

---