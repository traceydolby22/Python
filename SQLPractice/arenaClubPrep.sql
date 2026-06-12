SELECT users.name, COALESCE(SUM(orders.total_price), 0) AS total_spent 
FROM users
LEFT JOIN orders ON users.user_id = orders.user_id 
AND orders.status = 'completed'
GROUP BY users.name
ORDER BY total_spent DESC


/*Query:
Return each user's name and the total amount they've spent on completed orders only. Include users even if they have no completed orders — show 0 for them.
Sort highest spender first.*/
SELECT users.name, COALESCE(SUM(orders.price), 0) AS total_spent FROM users
LEFT JOIN orders on users.user_id = orders.user_id
AND orders.status = 'completed' 
GROUP BY users.name
ORDER BY total_spent DESC

/*Query 1: Return all available items.*/
Select * from items
where status = 'available'
/*Query 2: Return the name and price of all items in the cards category.*/
select name, price from items
where category = 'cards'
/*Query 3: Return the total number of sold items.*/
select count(*) as total_number from items
where status = 'sold'
/*Query 4: Return the total revenue from sold items.*/
select sum(price) as total_revenue from items
where status = 'sold'
/*Query 5: Return the count of items per category.*/
select count(*) as count from items 
group by category

/*Query: Return each customer's name and the total 
they've spent on completed orders. Include all customers 
even if they have no completed orders — show 0 for them.*/
select name From customers
join orders on customers.customer_id  = orders.customer_id
where status = 'completed'

