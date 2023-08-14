SELECT 
  teacher_id, 
  COUNT(
    DISTINCT(subject_id)
  ) AS cnt 
From 
  Teacher 
GROUP BY 
  teacher_id;
