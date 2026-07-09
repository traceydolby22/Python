SELECT (SELECT DISTINCT salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1
) AS second_highest_salary
/* with DISTINCT, your sorted list collapses the two 
79000 entries into a single value, so the ordered list becomes 
110000, 95000, 79000, 71000 instead of 110000, 95000, 79000, 79000, 71000
By wrapping your SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1 
inside that outer SELECT ( ... ), you change what's happening. Instead of asking 
"give me all matching rows," you're now asking "give me ONE single value — 
whatever this inner calculation produces, or NULL if it produces nothing at all." 
That outer SELECT (...) pattern, when the inner query returns zero rows, 
automatically resolves to NULL instead of an empty result. */