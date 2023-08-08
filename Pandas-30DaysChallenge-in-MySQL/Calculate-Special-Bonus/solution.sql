SELECT 
  employee_id, 
  salary AS bonus 
FROM 
  Employees 
WHERE 
  MOD(employee_id, 2) <> 0 
  AND name NOT LIKE "M%" 
UNION ALL 
SELECT 
  employee_id, 
  salary = (salary - salary) as bonus 
FROM 
  Employees 
WHERE 
  MOD(employee_id, 2) = 0 
  OR name LIKE "M%" 
ORDER BY 
  employee_id;
