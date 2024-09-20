SELECT id, CASE 
WHEN p_id IS NULL THEN 'Root'
WHEN p_id IS NOT NULL and id IN (SELECT DISTINCT p_id FROM TREE) THEN 'Inner'
ELSE 'Leaf'
END AS type
FROM Tree t1