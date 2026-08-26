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
    meansDebtBondageEarnings BOOLEAN,
    meansThreats BOOLEAN,
    meansAbusePsyPhySex BOOLEAN,
    meansFalsePromises BOOLEAN,
    meansDrugsAlcohol BOOLEAN,
    meansDenyBasicNeeds BOOLEAN,
    meansExcessiveWorkHours BOOLEAN,
    meansWithholdDocs BOOLEAN
);

-- 3. TABEL DIMENSI: Jenis & Sektor Eksploitasi
CREATE TABLE dim_exploitation (
    exploitation_id SERIAL PRIMARY KEY,
    isForcedLabour BOOLEAN,
    isSexualExploit BOOLEAN,
    isOtherExploit BOOLEAN,
    sectorOfLabourAgriculture BOOLEAN,
    sectorOfLabourConstruction BOOLEAN,
    sectorOfLabourDomesticWork BOOLEAN,
    sectorOfLabourHospitality BOOLEAN,
    sectorOfSexProstitution BOOLEAN,
    sectorOfSexPornography BOOLEAN
);

-- 4. TABEL DIMENSI: Hubungan Perekrut
CREATE TABLE dim_recruiter (
    recruiter_id SERIAL PRIMARY KEY,
    recruiterRelationIntimatePartner BOOLEAN,
    recruiterRelationFriend BOOLEAN,
    recruiterRelationFamily BOOLEAN,
    recruiterRelationOther BOOLEAN
);

-- 5. FACT TABLE: Tabel Utama yang Menghubungkan Semua Dimensi (Foreign Keys)
CREATE TABLE fact_trafficking_cases (
    case_id SERIAL PRIMARY KEY,
    yearOfRegistration VARCHAR(10),
    traffickMonths VARCHAR(50),
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
