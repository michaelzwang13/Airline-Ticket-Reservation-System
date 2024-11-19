SELECT * 
FROM flight
WHERE departure_date > CURDATE() or (departure_date = CURDATE() and departure_time > CURTIME());


SELECT * 
FROM flight
WHERE flight_status ='Delayed';


SELECT distinct first_name,last_name
FROM customer
WHERE customer.email_address in (SELECT distinct email_address
                                FROM purchase);


SELECT *
FROM airplane
WHERE airline_name = 'JetBlue Airways';