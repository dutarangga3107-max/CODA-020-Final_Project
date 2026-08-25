-- tabel schema

-- 1. TABEL DIMENSI: Demografi & Lokasi Korban
CREATE TABLE dim_demographics (
    demographic_id SERIAL PRIMARY KEY,
    gender VARCHAR(50),
    agebroad VARCHAR(50),
    citizenship VARCHAR(100),
    CountryOfExploitation VARCHAR(100)
);

-- 2. TABEL DIMENSI: Metode Pelaku (Means)
CREATE TABLE dim_means (
    means_id SERIAL PRIMARY KEY,
    meansDebtBondageEarnings INT,
    meansThreats INT,
    meansAbusePsyPhySex INT,
    meansFalsePromises INT,
    meansDrugsAlcohol INT,
    meansDenyBasicNeeds INT,
    meansExcessiveWorkHours INT,
    meansWithholdDocs INT
);

-- 3. TABEL DIMENSI: Jenis & Sektor Eksploitasi
CREATE TABLE dim_exploitation (
    exploitation_id SERIAL PRIMARY KEY,
    isForcedLabour INT,
    isSexualExploit INT,
    isOtherExploit INT,
    sectorOfLabourAgriculture INT,
    sectorOfLabourConstruction INT,
    sectorOfLabourDomesticWork INT,
    sectorOfLabourHospitality INT,
    sectorOfSexProstitution INT,
    sectorOfSexPornography INT
);

-- 4. TABEL DIMENSI: Hubungan Perekrut
CREATE TABLE dim_recruiter (
    recruiter_id SERIAL PRIMARY KEY,
    recruiterRelationIntimatePartner INT,
    recruiterRelationFriend INT,
    recruiterRelationFamily INT,
    recruiterRelationOther INT
);

-- 5. FACT TABLE: Tabel Utama yang Menghubungkan Semua Dimensi (Foreign Keys)
CREATE TABLE fact_trafficking_cases (
    case_id SERIAL PRIMARY KEY,
    yearOfRegistration INT,
    traffickMonths INT,
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

drop table dim_demographics, dim_means, dim_recruiter, dim_exploitation, fact_trafficking_cases;