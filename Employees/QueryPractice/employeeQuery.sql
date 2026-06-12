SELECT name, salary FROM employees 
WHERE status = 'active'

SELECT name FROM employees 
WHERE years > 4 AND status = 'active'

/*Return the total salary paid per department for active employees only.*/

SELECT department, SUM(salary) AS total_salary FROM employees
WHERE status = 'active'
GROUP BY department

/*Return all employees sorted by salary highest to lowest. Show name, department and salary. */

SELECT name, department, salary FROM employees
ORDER BY salary DESC

SELECT customer, product FROM orders
WHERE status = 'refunded'

SELECT * FROM orders 
WHERE status = 'completed' AND price > 100

SELECT category, SUM(price * quantity) AS total_revenue FROM orders
WHERE status = 'completed'
GROUP BY category

SELECT customer, product, price FROM orders
ORDER BY price DESC