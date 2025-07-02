# Write your MySQL query statement below
SELECT 
    patient_id, 
    patient_name, 
    conditions
FROM 
    Patients
WHERE 
    conditions LIKE BINARY 'DIAB1%' 
    OR conditions LIKE BINARY '% DIAB1%';