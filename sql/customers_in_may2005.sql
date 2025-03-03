SELECT customer.first_name, customer.last_name
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
WHERE rental_date >= '2005-05-01' AND rental_date < '2006-06-01'