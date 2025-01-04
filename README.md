# Airline Ticket Reservation System

## Project Overview

This project was created to simulate an airline ticket reservation website 
with functionalities for both airline staff and customers. Each has its
own unique features and all actions and transactions are managed using a
database system. 

Customer:
- Register and login/logout with md5 password encryption for security
- Search flights and check flight status 
- Purchase and cancel flight tickets
- Check previous and upcoming flights
- Rate previous flights
- Track spending within specified time range
- Edit profile information

Staff:
- Register and login/logout with md5 password encryption for security
- Search flights and check flight status 
- View upcoming flights under the airline the staff member works for
- View all customers on a specific flight
- Sort flights based on status
- Create new flights and change statuses of flights
- Add new airports and airplanes to the database
- Schedule maintenances for airplanes
- View flight ratings and frequent customers
- View revenue over a specified time range
- Edit profile information

### Project Snippets
![Customer Login Page](/src/demo/image1.png)
![Customer Register Page](/src/demo/image2.png)
![Flight Search Interface](/src/demo/image3.png)
![Flight Search Results](/src/demo/image4.png)
![Staff View Monthly Revenue](/src/demo/image5.png)

### Languages and Tools
1. Frontend: HTML/CSS and JavaScript
2. Backend: Flask (Python) and MySQL
3. Database Management System: Apache Web Server with phpMyAdmin

### How to Run 
1. Ensure database name and port are matching
2. Install all dependencies ```pip3 install -r requirements.txt```
3. Start the server 
4. Run the query in inserts.sql on phpMyAdmin to create the tables and insert data
5. Run ```python3 project.py``` to start the server