## **HUMAN TRAFICKING ANALYSIS**

## **Data Engineering (Pipeline & Infrastructure)**

## **Background**
kasus Tindak Pidana Perdagangan Orang (TPPO) dan eksploitasi pekerja migran lintas negara seperti sindikat penipuan kerja ilegal berkedok tawaran gaji tinggi di luar negeri serta jeratan kerja paksa tanpa prosedur resmi menunjukkan bahwa human trafficking masih menjadi krisis kemanusiaan global yang kompleks.

Kejahatan ini didorong oleh berbagai faktor multi-dimensi, mulai dari kerentanan demografis korban, risiko spesifik sektor pekerjaan, hingga dinamika trust (kepercayaan) yang dimanipulasi oleh pelaku termasuk kasus di mana identitas atau jaringan pelaku tidak terdeteksi oleh sistem hukum. Memahami bagaimana elemen-elemen ini saling beririsan, khususnya bagaimana pelaku memanfaatkan hubungan kedekatan emosional (seperti keluarga, teman, atau mitra) untuk menjebak korban, sangat krusial untuk mengidentifikasi segmen berisiko tinggi. Dengan menganalisis data korban secara komprehensif, proyek ini bertujuan untuk mengungkap pola kerentanan tersembunyi, sehingga para pemangku kepentingan dapat merancang intervensi yang tepat sasaran dan berbasis data.
## **Fenomena**
Perkembangan Media Sosial dan Online Platforms semakin mempermudah traffickers dalam menemukan, mendekati, dan memanipulasi calon korban. Namun, recruitment tidak selalu dilakukan oleh orang asing. Hubungan dekat seperti keluarga, teman atau pasangan dapat menjadi jalur recruitment karena adanya kepercayaan dan kedekatan interpersonal. oleh karena itu, diperlukan analisis untuk mengetahui kelompok korban mana yang paling rentan, sektor eksploitasi apa yang paling berisiko, serta apakah hubungan korban dengan bentuk dan tingkat eksploitasi yang dialami.

## Stakeholder

Proyek ini melibatkan berbagai stakeholder yang memiliki peran dalam pencegahan human trafficking, perlindungan korban, penegakan hukum, serta pengembangan kebijakan dan strategi berbasis data.

| Stakeholder | Peran |
|---|---|
| **United Nations (UN)** | Mengembangkan kerangka kerja internasional, kebijakan, dan kerja sama dalam penanganan perdagangan manusia serta perlindungan hak asasi manusia | 
| **Kepolisian / Aparat Penegak Hukum** | Melakukan penyelidikan kasus, mengidentifikasi pelaku dan jaringan perdagangan manusia, serta mendukung proses penegakan hukum | 
| **UNICEF** | Melindungi anak dari perdagangan manusia, eksploitasi, kekerasan, dan bentuk pelanggaran lainnya | Tinggi |
| **Perusahaan Platform Media Sosial** | Mendeteksi dan mencegah aktivitas terkait perdagangan manusia serta meningkatkan keamanan dan mekanisme pelaporan di platform | 
| **Researchers / Peneliti** | Menganalisis pola perdagangan manusia, mengidentifikasi faktor risiko, dan menghasilkan temuan berbasis data untuk mendukung kebijakan | 

## **SDG**

| SDG | Fokus | Keterkaitan dengan Human Trafficking |
|---|---|---|
| **SDG 5** | Kesetaraan Gender | Mengatasi kerentanan berbasis gender serta eksploitasi seksual dalam perdagangan manusia |
| **SDG 8** | Pekerjaan Layak dan Pertumbuhan Ekonomi | Mengatasi forced labour dan eksploitasi tenaga kerja serta mendukung kondisi kerja yang layak |
| **SDG 10** | Berkurangnya Kesenjangan | Mengurangi kerentanan kelompok sosial dan ekonomi tertentu terhadap perdagangan dan eksploitasi |
| **SDG 16** | Perdamaian, Keadilan dan Kelembagaan yang Tangguh | Mendukung perlindungan hak asasi manusia, penegakan hukum, perlindungan korban, dan penguatan institusi |

## **Data Dictionary**

### A. DEMOGRAPHICS

| Column | Data Type | Definisi |
|---|---|---|
| `demographic_id` | serial | Primary key yang menjadi identitas unik setiap data demografi korban |
| `gender` | varchar(50) | Gender korban |
| `agebroad` | varchar(50) | Kelompok usia korban |
| `citizenship` | varchar(100) | Kewarganegaraan korban |
| `countryofexploitation` | varchar(100) | Negara tempat korban mengalami eksploitasi |

---

### B. EXPLOITATION

| Column | Data Type | Definisi |
|---|---|---|
| `exploitation_id` | serial | Primary key yang menjadi identitas unik setiap data eksploitasi |
| `isforcedlabour` | boolean | Menunjukkan apakah korban mengalami forced labour |
| `issexualexploit` | boolean | Menunjukkan apakah korban mengalami eksploitasi seksual |
| `isotherexploit` | boolean | Menunjukkan apakah korban mengalami bentuk eksploitasi lainnya |
| `sectoroflabouragriculture` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan sektor pertanian |
| `sectoroflabourconstruction` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan sektor konstruksi |
| `sectoroflabourdomesticwork` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan pekerjaan domestik |
| `sectoroflabourhospitality` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan sektor hospitality |
| `sectorofsexprostitution` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan sektor prostitusi |
| `sectorofsexpornography` | boolean | Menunjukkan apakah eksploitasi berkaitan dengan sektor pornografi |

---

### C. MEANS

| Column | Data Type | Definisi |
|---|---|---|
| `means_id` | serial | Primary key yang menjadi identitas unik setiap data metode eksploitasi |
| `meansdebtbondageearnings` | boolean | Menunjukkan penggunaan debt bondage atau keterikatan melalui utang/penghasilan dalam eksploitasi |
| `meansthreats` | boolean | Menunjukkan penggunaan ancaman terhadap korban |
| `meansabusepsyphysex` | boolean | Menunjukkan adanya penyalahgunaan atau kekerasan psikologis, fisik, atau seksual |
| `meansfalsepromises` | boolean | Menunjukkan penggunaan janji palsu dalam proses recruitment atau eksploitasi |
| `meansdrugsalcohol` | boolean | Menunjukkan keterlibatan drugs atau alcohol dalam proses eksploitasi |
| `meansdenybasicneeds` | boolean | Menunjukkan adanya pembatasan atau penolakan kebutuhan dasar korban |
| `meansexcessiveworkhours` | boolean | Menunjukkan pemberian jam kerja yang berlebihan kepada korban |
| `meanswithholddocs` | boolean | Menunjukkan adanya penahanan dokumen pribadi korban |

---

### D. RECRUITER

| Column | Data Type | Definisi |
|---|---|---|
| `recruiter_id` | serial | Primary key yang menjadi identitas unik setiap data hubungan recruiter |
| `recruiterrelationintimatepartner` | boolean | Menunjukkan apakah recruiter merupakan pasangan atau intimate partner korban |
| `recruiterrelationfriend` | boolean | Menunjukkan apakah recruiter merupakan teman korban |
| `recruiterrelationfamily` | boolean | Menunjukkan apakah recruiter memiliki hubungan keluarga dengan korban |
| `recruiterrelationother` | boolean | Menunjukkan apakah recruiter memiliki hubungan lainnya dengan korban |

---

### E. TRAFFICKING CASES

| Column | Data Type | Definisi |
|---|---|---|
| `case_id` | serial | Primary key yang menjadi identitas unik setiap kasus trafficking |
| `yearofregistration` | varchar(10) | Tahun ketika kasus trafficking dicatat atau diregistrasikan |
| `traffickmonths` | varchar(50) | Durasi korban mengalami trafficking atau eksploitasi dalam bulan |
| `demographic_id` | integer | Foreign key yang menghubungkan kasus dengan data demografi korban |
| `means_id` | integer | Foreign key yang menghubungkan kasus dengan metode eksploitasi |
| `exploitation_id` | integer | Foreign key yang menghubungkan kasus dengan bentuk dan sektor eksploitasi |
| `recruiter_id` | integer | Foreign key yang menghubungkan kasus dengan hubungan recruiter |

## **Problem Statement**
Sulitnya mengidentifikasi kelompok korbann, sektor pekerjaan, dan pola recruitement yang memiliki resiko exploitasi lebih tinggi, serta memahami bagaimana karakteristik tersebut berkiatan dengan bentuk eksploitasi yang dialami korban. Belum diketahui apakah hubungan tertentu antara korban dan recruiter berkaitan dengan tingkat eksploitasi yang lebih tinggi dan kelompok demografis mana yang paling rentan terhadap pola recruitement tersebut.
| SMART          | Framework                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Specific**   | Mengidentifikasi **kelompok demografis, sektor eksploitasi, recruitment relationship, dan bentuk eksploitasi** yang memiliki tingkat risiko lebih tinggi, serta mengetahui hubungan recruiter mana yang paling sering berujung pada **forced labour atau sexual exploitation**. Selain itu, menganalisis tingkat kontrol yang dialami korban berdasarkan **8 bentuk means of control**.                                                                                                                                                                                            |
| **Measurable** | Mengukur risiko menggunakan **jumlah korban (count), persentase korban (%), dan exploitation rate (%)** berdasarkan `ageBroad`, `gender`, `citizenship`, sektor, dan recruitment relationship. Hubungan recruiter juga dibandingkan berdasarkan proporsi korban yang mengalami **forced labour, sexual exploitation, dan other exploitation**. Tingkat kontrol korban diukur dengan menjumlahkan **8 kolom `means`**, sehingga setiap korban memiliki **Control Means Score 0–8**. Contohnya, korban dengan nilai **6/8** berarti mengalami 6 dari 8 bentuk kontrol yang tercatat. |
| **Achievable** | Analisis dapat dilakukan berdasarkan variabel yang tersedia dalam dataset, yaitu karakteristik demografis, sektor eksploitasi, recruitment relationship, exploitation outcome, dan 8 indikator means of control. Analisis menggunakan **descriptive statistics, cross-tabulation, persentase, exploitation rate, dan Chi-Square Test** untuk melihat hubungan antarvariabel.                                                                                                                                                                                                       |
| **Relevant**   | Hasil analisis dapat membantu **United Nations, kepolisian, UNICEF, platform media sosial, dan researchers** mengidentifikasi kelompok yang lebih rentan, recruitment relationship yang lebih sering berkaitan dengan bentuk eksploitasi tertentu, serta tingkat kontrol yang dialami korban. Informasi ini dapat mendukung strategi **pencegahan, identifikasi, perlindungan korban, dan penegakan hukum**.                                                                                                                                                                       |
| **Time-Bound** | Analisis mencakup kasus yang tercatat dalam dataset selama periode **2002–2024**. Perubahan jumlah korban, pola recruitment relationship, sektor, bentuk eksploitasi, dan tingkat kontrol dapat dibandingkan berdasarkan tahun registrasi untuk melihat **tren selama 23 tahun**. Hasil historis tersebut dapat menjadi dasar untuk analisis dan proyeksi pola trafficking di periode berikutnya.                                                                                                                                                                                  |

## **Key Questions**
1. Kelompok demografis mana yang memiliki resiko eksploitasi tertinggi berdasarkan usia, gender, dan citizhenship?
2. Sektor mana saja yang paling rentan terhadap eksploitasi, dan bentuk eksploitasi apa yang paling banyak terjadi di sektor tersebut?
3. Apakah hubungan antara korban dan recruiter berkaitan dengan perbedaan resiko dan bentuk eksploitasi yang dialami korban?
4. Kelompok usia dan gender mana yang paling sering direkrut melalui hubungan dekat seperti family, friend, atau intimate partner, dan bagaimana tingkat eksploitasi kelompok tersebut?
5. Kombinasi faktor demografis, sektor pekerajaan, dan recruitemnt relationship seperti apa yang membentuk profil korban dengan resiko eksploitasi paling tinggi?
6. Bagaimana tren jumlah korban berdasarkan recruitment relationship dari tahun ke tahun?


## **Key Performance Indicators (KPI)**
**1. Exploitation Rate**<br>
**Explanation:** Mengukur persentase korban yang mengalami forced labour dari total korban.<br>
**Purpose:** Mengetahui proporsi keseluruhan korban yang mengalami eksploitasi.
  
**2. Forced Labour Rate**<br>
**Explanation:** Mengukur persentase korban yang mengalami forced labour dari total korban.<br>
**Purpose:** Mengidentifikasi seberapa sering kasus kerja paksa terjadi dalam dataset ini. 
  
**3. Sexual Exploitation Rate**<br>
**Explanation:** Mengukur persentase korban yang mengalami sexual exploitation dari total korban.<br>
**Purpose:** Mengetahui seberapa besar proporsi korban yang mengalami eksploitasi seksual.
  
**4. Debt Bondage Rate**<br>
**Explanation:** Mengukur persentase korban yang mengalami debt bondage dari total korban.<br>
**Purpose:** Mengidentifikasi tingkat eksploitasi yang berkaitan dengan keterikatan utang.
  
**5. Document Withholding Rate**<br>
**Explanation:** Mengukur persentase korban yang mengalami penahanan atau penyitaan dokumen dari total korban.<br>
**Purpose:** Mengetahui seberapa sering terjadi penahanan dokumen sebagao salah satu indikator resiko eksploitasi.
  
**6. High-Risk Sector Agriculture**<br>
**Explanation:** Mengukur exploitation rate khusus pada korban yang bekerja di sektor Agriculture.<br>
**Purpose:** Mengidentifikasi apakah sektor Agricukture merupakan sektor dengan resiko eksploitasi yang tinggi.
  
**7. High-Risk Age**<br>
**Explanation:** Menemukan kelompok usia dengan exploitation rate tertinggi.<br>
**Purpose:** Mengidentifikasi kelompok usia yang paling rentan terhadap eksploitasi.
  
**8. High-Risk Citizenship**<br>
**Explanation:** Mengukur exploitation rate berdasarkan kewarganegaraan korban.<br>
**Purpose:** Mengidentifikasi kelompok kewarganegaraan dengan tingkat resiko eksploitasi tertinggi.
  
**9. Recruitement Risk**<br>
**Explanation:** Mengukur exploitation rate berdasarkan recruitment relationship atau hubungan antara korban dan pihak yang merekrutnya.<br>
**Purpose:** Mengidentifikasi pola hubungan rekrutmen yang memiliki tingkat resiko eksploitasi lebih tinggi.

### cara run
**Isi koneksi** : isi url_database_neon di FP_load.py, lalu copy file dan paste ke `airflow_spark/scripts/`
**selanjut nya bisa baca readme di folder airflow**
