## **FINAL PROJCET HUMAN TRAFICKING ANALYSIS**

## **Data Engineering (Pipeline & Infrastructure)**

## **Background**
Labour dan sexual exploitation dipengaruhi oleh berbagai faktor, seperti karakteristik demografis korban, sektor pekerjaan, jenis eksploitasi, dan pola recruitment. Data korban dapat dimanfaatkan untuk mengidentifikasi pola dan faktor resiko, termasuk menganalisis apakah hubungan korban dengan recruiter seperti keluarga, teman, atau stranger berkaitan dengan tingkat dan bentuk eksploitasi yang dialami. Analaisi ini membantu menemukan kelompok dan kondisi yang paling rentan sehingga intevensi dapat dilakukan secara tepat sasaran.

## **Fenomena**
Perkembangan Media Sosial dan Online Platforms semakin mempermudah traffickers dalam menemukan, mendekati, dan memanipulasi calon korban. Namun, recruitment tidak selalu dilakukan oleh orang asing. Hubungan dekat seperti keluarga, teman atau pasangan dapat menjadi jalur recruitment karena adanya kepercayaan dan kedekatan interpersonal. oleh karena itu, diperlukan analisis untuk mengetahui kelompok korban mana yang paling rentan, sektor eksploitasi apa yang paling berisiko, serta apakah hubungan korban dengan bentuk dan tingkat eksploitasi yang dialami.

## Stakeholder

Proyek ini melibatkan berbagai stakeholder yang memiliki peran dalam pencegahan human trafficking, perlindungan korban, penegakan hukum, serta pengembangan kebijakan dan strategi berbasis data.

| Stakeholder | Peran | Kepentingan terhadap Proyek |
|---|---|---|
| **United Nations (UN)** | Mengembangkan kerangka kerja internasional, kebijakan, dan kerja sama dalam penanganan perdagangan manusia serta perlindungan hak asasi manusia | Tinggi |
| **Kepolisian / Aparat Penegak Hukum** | Melakukan penyelidikan kasus, mengidentifikasi pelaku dan jaringan perdagangan manusia, serta mendukung proses penegakan hukum | Tinggi |
| **UNICEF** | Melindungi anak dari perdagangan manusia, eksploitasi, kekerasan, dan bentuk pelanggaran lainnya | Tinggi |
| **Perusahaan Platform Media Sosial** | Mendeteksi dan mencegah aktivitas terkait perdagangan manusia serta meningkatkan keamanan dan mekanisme pelaporan di platform | Tinggi |
| **Researchers / Peneliti** | Menganalisis pola perdagangan manusia, mengidentifikasi faktor risiko, dan menghasilkan temuan berbasis data untuk mendukung kebijakan | Sedang–Tinggi |

## **SDG**

| SDG | Fokus | Keterkaitan dengan Human Trafficking |
|---|---|---|
| **SDG 5** | Kesetaraan Gender | Mengatasi kerentanan berbasis gender serta eksploitasi seksual dalam perdagangan manusia |
| **SDG 8** | Pekerjaan Layak dan Pertumbuhan Ekonomi | Mengatasi forced labour dan eksploitasi tenaga kerja serta mendukung kondisi kerja yang layak |
| **SDG 10** | Berkurangnya Kesenjangan | Mengurangi kerentanan kelompok sosial dan ekonomi tertentu terhadap perdagangan dan eksploitasi |
| **SDG 16** | Perdamaian, Keadilan dan Kelembagaan yang Tangguh | Mendukung perlindungan hak asasi manusia, penegakan hukum, perlindungan korban, dan penguatan institusi |

## **Data Dictionary**

### A. Demographic Variables

| Column | Data Type | Definisi |
|---|---|---|
| `ageBroad` | str | Kelompok usia korban |
| `gender` | str | Gender korban |
| `citizenship` | str | Kewarganegaraan korban |

### B. Recruitment Relationship

| Column | Data Type | Definisi |
|---|---|---|
| `recruiterRelationFamily` | bool | Indikator apakah recruiter memiliki hubungan keluarga dengan korban |
| `recruiterRelationFriend` | bool | Indikator apakah recruiter merupakan teman korban |
| `recruiterRelationIntimatePartner` | bool | Indikator apakah recruiter merupakan pasangan atau intimate partner korban |
| `recruiterRelationOther` | bool | Indikator apakah recruiter memiliki hubungan lain dengan korban atau tidak memiliki hubungan |

### C. Sector

| Column | Data Type | Definisi |
|---|---|---|
| `sectorOfLabourAgriculture` | bool | Indikator apakah eksploitasi berkaitan dengan sektor pertanian |
| `sectorOfLabourConstruction` | bool | Indikator apakah eksploitasi berkaitan dengan sektor konstruksi |
| `sectorOfLabourDomesticWork` | bool | Indikator apakah eksploitasi berkaitan dengan pekerjaan domestik |
| `sectorOfLabourHospitality` | bool | Indikator apakah eksploitasi berkaitan dengan sektor hospitality |
| `sectorOfSexProstitution` | bool | Indikator apakah eksploitasi berkaitan dengan prostitusi |
| `sectorOfSexPornography` | bool | Indikator apakah eksploitasi berkaitan dengan pornografi |

### D. Exploitation Outcome

| Column | Data Type | Definisi |
|---|---|---|
| `isForcedLabour` | bool | Indikator apakah korban mengalami forced labour |
| `isSexualExploit` | bool | Indikator apakah korban mengalami eksploitasi seksual |
| `isOtherExploit` | bool | Indikator apakah korban mengalami bentuk eksploitasi lainnya |

### E. Means Outcome

| Column | Data Type | Definisi |
|---|---|---|
| `meansDebtBondageEarning` | bool | Indikator apakah debt bondage atau keterikatan melalui utang/penghasilan digunakan sebagai metode eksploitasi |
| `meansThreats` | bool | Indikator apakah ancaman digunakan dalam proses trafficking atau eksploitasi |
| `meansAbusePsyPhysSex` | bool | Indikator apakah kekerasan atau penyalahgunaan psikologis, fisik, atau seksual digunakan |
| `meansFalsePromises` | bool | Indikator apakah janji palsu digunakan untuk merekrut atau mengeksploitasi korban |
| `meansDrugsAlcohol` | bool | Indikator apakah drugs/alcohol terlibat dalam proses eksploitasi |
| `meansDenyBasicNeeds` | bool | Indikator apakah kebutuhan dasar korban ditolak atau dibatasi |
| `meansExcessiveWorkHours` | bool | Indikator apakah korban diberikan jam kerja yang berlebihan |
| `meansWithholdDocs` | bool | Indikator apakah dokumen pribadi korban ditahan |

### F. Supporting Variables

| Column | Data Type | Definisi |
|---|---|---|
| `traffickMonths` | str | Durasi korban mengalami trafficking atau eksploitasi dalam bulan |
| `CountryOfExploitation` | str | Negara tempat korban mengalami eksploitasi |
| `yearOfRegistration` | float64 | Tahun ketika kasus korban dicatat atau diregistrasikan |

## **Problem Statement**
Sulitnya mengidentifikasi kelompok korbann, sektor pekerjaan, dan pola recruitement yang memiliki resiko exploitasi lebih tinggi, serta memahami bagaimana karakteristik tersebut berkiatan dengan bentuk eksploitasi yang dialami korban. Belum diketahui apakah hubungan tertentu antara korban dan recruiter berkaitan dengan tingkat eksploitasi yang lebih tinggi dan kelompok demografis mana yang paling rentan terhadap pola recruitement tersebut.

## **Key Questions**
1. Kelompok demografis mana yang memiliki resiko eksploitasi tertinggi berdasarkan usia, gender, dan citizhenship?
2. Sektor mana saja yang paling rentan terhadap eksploitasi, dan bentuk eksploitasi apa yang paling banyak terjadi di sektor tersebut?
3. Apakah hubungan antara korban dan recruiter berkaitan dengan perbedaan resiko dan bentuk eksploitasi yang dialami korban?
4. Kelompok usia dan gender mana yang paling sering direkrut melalui hubungan dekat seperti family, friend, atau intimate partner, dan bagaimana tingkat eksploitasi kelompok tersebut?
5. Kombinasi faktor demografis, sektor pekerajaan, dan recruitemnt relationship seperti apa yang membentuk profil korban dengan resiko eksploitasi paling tinggi?

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
