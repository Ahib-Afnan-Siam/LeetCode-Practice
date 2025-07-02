SELECT 
    user_id, 
    name, 
    mail 
FROM 
    Users 
WHERE 
    mail LIKE BINARY '%@leetcode.com' 
    AND mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';