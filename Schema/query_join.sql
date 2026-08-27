-- key question

-- join fact table & demografi
CREATE VIEW analisis_demografi AS
SELECT 
    f.case_id,
    f.yearofregistration,
    f.traffickmonths,
    d.gender,
    d.agebroad,
    d.citizenship,
    d.countryofexploitation
FROM fact_trafficking_cases f
JOIN dim_demographics d ON f.demographic_id = d.demographic_id;

-- join fact table & exploitation
CREATE VIEW analisis_sektor_eksploitasi AS
SELECT 
    f.case_id,
    f.yearofregistration,
    e.isforcedlabour,
    e.issexualexploit,
    e.isotherexploit,
    e.sectoroflabouragriculture,
    e.sectoroflabourdomesticwork,
    e.sectoroflabourhospitality,
    e.sectorsexprostitution,
    e.sectorsexpornography
FROM fact_trafficking_cases f
JOIN dim_exploitation e ON f.exploitation_id = e.exploitation_id;

-- join fact table & recruiter 
CREATE VIEW analisis_rekrutmen AS
SELECT 
    f.case_id,
    f.yearofregistration,
    r.recruiterrelationintimatepartner,
    r.recruiterrelationfriend,
    r.recruiterrelationfamily,
    r.recruiterrelationother
FROM fact_trafficking_cases f
JOIN dim_recruiter r ON f.recruiter_id = r.recruiter_id;

-- KPI 

CREATE VIEW v_all_key_questions_complete AS
SELECT 
    f.case_id,
    f.yearofregistration,
    f.traffickmonths,
    d.agebroad,
    d.gender,
    d.citizenship,
    e.isforcedlabour,
    e.issexualexploit,
    e.isotherexploit,
    e.sectoroflabouragriculture,
    e.sectoroflabourconstruction,
    e.sectoroflabourdomesticwork,
    e.sectoroflabourhospitality,
    e.sectorofsexprostitution,
    e.sectorofsexpornography,
    m.meansdebtbondageearnings,
    m.meanswithholddocs,
    r.recruiterrelationintimatepartner,
    r.recruiterrelationfriend,
    r.recruiterrelationfamily,
    r.recruiterrelationother
FROM fact_trafficking_cases f
LEFT JOIN dim_demographics d ON f.demographic_id = d.demographic_id
LEFT JOIN dim_exploitation e ON f.exploitation_id = e.exploitation_id
LEFT JOIN dim_means m ON f.means_id = m.means_id
LEFT JOIN dim_recruiter r ON f.recruiter_id = r.recruiter_id;

