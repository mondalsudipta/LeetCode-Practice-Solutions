-- solution 1 :

SELECT 
  class 
FROM 
  (
    SELECT 
      class, 
      COUNT(student) AS num 
    FROM 
      courses 
    GROUP BY 
      class
  ) AS temp_table 
WHERE 
  num >= 5;


-- solution 2 :

SELECT 
  class 
FROM 
  Courses 
GROUP BY 
  class 
HAVING 
  COUNT(student) >= 5;
