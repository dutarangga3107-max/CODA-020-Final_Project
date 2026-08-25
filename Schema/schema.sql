-- tabel schema

-- 1. TABEL DIMENSI: Demografi & Lokasi Korban
CREATE TABLE dim_demographics (
    demographic_id SERIAL PRIMARY KEY,
    gender VARCHAR(50),
    age_broad VARCHAR(50),
    citizenship VARCHAR(100),
    country_of_exploitation VARCHAR(100)
);

-- 2. TABEL DIMENSI: Metode Pelaku (Means)
CREATE TABLE dim_means (
    means_id SERIAL PRIMARY KEY,
    means_debt_bondage INT,
    means_threats INT,
    means_abuse INT,
    means_false_promises INT,
    means_drugs_alcohol INT,
    means_deny_basic_needs INT,
    means_excessive_work_hours INT,
    means_withhold_docs INT
);

-- 3. TABEL DIMENSI: Jenis & Sektor Eksploitasi
CREATE TABLE dim_exploitation (
    exploitation_id SERIAL PRIMARY KEY,
    is_forced_labour INT,
    is_sexual_exploit INT,
    is_other_exploit INT,
    sector_agriculture INT,
    sector_construction INT,
    sector_domestic_work INT,
    sector_hospitality INT,
    sector_prostitution INT,
    sector_pornography INT
);

-- 4. TABEL DIMENSI: Hubungan Perekrut
CREATE TABLE dim_recruiter (
    recruiter_id SERIAL PRIMARY KEY,
    recruiter_intimate_partner INT,
    recruiter_friend INT,
    recruiter_family INT,
    recruiter_other INT
);

-- 5. FACT TABLE: Tabel Utama yang Menghubungkan Semua Dimensi (Foreign Keys)
CREATE TABLE fact_trafficking_cases (
    case_id SERIAL PRIMARY KEY,
    year_of_registration INT,
    traffick_months INT,
    demographic_id INT REFERENCES dim_demographics(demographic_id),
    means_id INT REFERENCES dim_means(means_id),
    exploitation_id INT REFERENCES dim_exploitation(exploitation_id),
    recruiter_id INT REFERENCES dim_recruiter(recruiter_id)
);

select * from dim_demographics;
select * from dim_means;
select * from dim_recruiter;
select * from dim_exploitation;
select * from fact_trafficking_cases;