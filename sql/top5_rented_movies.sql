SELECT film.title, COUNT(rental.rental_id) AS number_times_rented
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title
ORDER BY COUNT(rental.rental_id) DESC
LIMIT 5