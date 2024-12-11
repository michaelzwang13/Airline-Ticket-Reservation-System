#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect, send_file
from datetime import date
import pymysql.cursors
import os
import sys
import hashlib
#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                        #port = 8889,
                        #user='root',
                        #password='root',
                        #db='ProjectFinal',
                        #charset='utf8mb4',
                        #cursorclass=pymysql.cursors.DictCursor)
                        port = 3306,
                        user='root',
                        password='',
                        db='demo_flight',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html',section = "search-flights") # set default to search flights

@app.route('/redirect_searchflights')
def redirect_searchflights():
    if 'email_address' in session.keys():
        email_address = session['email_address']
        return render_template('customer_home.html', email_address=email_address, section='search-flights')
    elif 'username' in session.keys():
        username = session['username']
        # results = staff_default_flights()
        # return render_template('staff_home.html', username=username, results = results,section='search-flights')
        return render_template('staff_home.html', username=username, section='search-flights')
    else:
        return render_template('index.html', section='search-flights')
    
@app.route('/redirect_checkstatus')
def redirect_checkstatus():
    if 'email_address' in session.keys():
        email_address = session['email_address']
        return render_template('customer_home.html', email_address=email_address, section='check-status')
    elif 'username' in session.keys():
        username = session['username']
        return render_template('staff_home.html', username=username, section='check-status')
    else:
        return render_template('index.html', section='check-status')

@app.route('/redirect_viewflights')
def redirect_viewflights():
    username = session['username']
    return render_template('staff_home.html', username=username, section='view-flights')

@app.route('/redirect_viewcustomers')
def redirect_viewcustomers():
    username = session['username']
    return render_template('staff_home.html', username=username, section='view-customers')
    
@app.route('/redirect_searchcustomer')
def redirect_searchcustomer():
    username = session['username']
    cursor = conn.cursor()
    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']
    cursor.close()

    freq_customer, revenue = get_revenue_mostFrequentCustomer(airline_name)
    customer = {"most":freq_customer}
    return render_template('staff_profile.html', username = username,customer = customer,revenue = revenue,section='view-frequent-customers')

@app.route('/redirect_searchrates')
def redirect_searchrates():
    username = session['username']

    cursor = conn.cursor()
    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']
    cursor.close()

    customer, revenue = get_revenue_mostFrequentCustomer(airline_name)
    return render_template('staff_profile.html', username = username,customer = customer,revenue = revenue,section='view-flight-rates')

@app.route('/redirectAddAirplane')
def redirectAddAirplane():
    return render_template('staff_manage.html',section = 'add-airplane')

#Define route for customer login
@app.route('/customer_login')
def customer_login():
    return render_template('customer_login.html')

#Define route for staff login
@app.route('/staff_login')
def staff_login():
    return render_template('staff_login.html')

#Define route for customer register
@app.route('/customer_register')
def customer_register():
    return render_template('customer_register.html')

#Define route for staff register
@app.route('/staff_register')
def staff_register():
    return render_template('staff_register.html')

#Authenticates the customer login
@app.route('/customerLoginAuth', methods=['GET', 'POST'])
def customerLoginAuth():
    #grabs information from the forms
    email_address = request.form['email_address']
    password = request.form['password']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM customer WHERE email_address = %s'
    cursor.execute(query, (email_address))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #if bcrypt.checkpw(password.encode('utf-8'), data['password'].encode('utf-8')):
        if hash_password_md5(password)==data['password']:
        #creates a session for the the user
        #session is a built in
            session['email_address'] = email_address
            return redirect(url_for('customer_home'))
        else:
            error = 'Invalid login or email_address'
            return render_template('customer_login.html', error=error)
            
    else:
           #returns an error message to the html page
        error = 'Invalid login or email_address'
        return render_template('customer_login.html', error=error)
    
@app.route('/staffLoginAuth', methods=['GET', 'POST'])
def staffLoginAuth():
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        #if bcrypt.checkpw(password.encode('utf-8'), data['password'].encode('utf-8')):
        if hash_password_md5(password)==data['password']:
            session['username'] = username
            return redirect(url_for('staff_home'))
        else:
            error = 'Invalid login or username'
            return render_template('staff_login.html', error=error)

    else:
        #returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('staff_login.html', error=error)
def hash_password_md5(password):
    # Create an MD5 hash object
    md5 = hashlib.md5()
    # Encode and hash the password
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

@app.route('/customerRegisterAuth', methods=['GET', 'POST'])
def customerRegisterAuth():
    #grabs information from the forms
    email_address = request.form['email_address']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    building_name = request.form['building_name']
    street_name = request.form['street_name']
    apt_num = request.form['apt_num']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']
    date_of_birth = request.form['date_of_birth']
    passport_number = request.form['passport_number']
    passport_expiration = request.form['passport_expiration']
    passport_country = request.form['passport_country']
    phone_number = []
    hashed_password = hash_password_md5(password)#bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    for key, value in request.form.items():
        if value !='':
            if 'phoneNumbers' in key:  # Handle array-style inputs for phone numbers
                phone_number.append(value)
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM customer WHERE email_address = %s'
    cursor.execute(query, (email_address))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This email already exists"
        return render_template('customer_register.html', error = error)
    else:
        ins = 'INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (email_address, hashed_password, first_name, last_name, building_name,
                            street_name, apt_num, city, state, zipcode, date_of_birth,
                            passport_number, passport_expiration, passport_country))
        ins_phone = 'INSERT INTO customer_phone_number VALUES(%s, %s)'
        for num in phone_number:
            cursor.execute(ins_phone, (email_address,num))
        conn.commit()
        cursor.close()
        session['email_address'] = email_address
        return render_template('customer_home.html',section='search-flights',email_address = email_address)

@app.route('/staffRegisterAuth', methods=['GET', 'POST'])
def staffRegisterAuth():
    #grabs information from the forms
    username = request.form['username']
    airline_name = request.form['airline_name']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    phone_number = []
    hashed_password = hash_password_md5(password)#bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    for key, value in request.form.items():
        if value !='':
            if 'phoneNumbers' in key:  # Handle array-style inputs for phone numbers
                phone_number.append(value)
    email_address = []
    for key, value in request.form.items():
        if value !='':
            if 'email_address' in key:  # Handle array-style inputs for phone numbers
                email_address.append(value)
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This username already exists"
        return render_template('staff_register.html', error = error)
    else:
        ins = 'INSERT INTO airline_staff VALUES(%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (username, airline_name, hashed_password, first_name, last_name, date_of_birth))
        ins_phone = 'INSERT INTO airline_staff_phone_number VALUES(%s, %s)'
        for num in phone_number:
            cursor.execute(ins_phone, (username,num))
        ins_email = 'INSERT INTO airline_staff_email VALUES(%s, %s)'
        for email in email_address:
            cursor.execute(ins_email, (username,email))
        conn.commit()
        cursor.close()
        session['username'] = username
        return render_template('staff_home.html',username=username, section='search-flights')
    

@app.route('/images/<path:filename>')
def get_image(filename):
    try:
        image_path = os.path.join('images', filename)
        return send_file(image_path, mimetype='image/jpeg')
    except FileNotFoundError:
        return "Image not found", 404

@app.route('/customer_home')
def customer_home():
    email_address = session['email_address']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM customer WHERE email_address = %s'
    cursor.execute(query, (email_address))
    data1 = cursor.fetchall() 
    cursor.close()
    
    return render_template('customer_home.html', email_address=email_address, posts=data1, section='search-flights')

@app.route('/staff_home')
def staff_home():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    cursor.close()
    return render_template('staff_home.html', username=username, posts=data1, section='search-flights')

@app.route('/staff_manage')
def staff_manage():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    cursor.close()
    return render_template('staff_manage.html', username=username,section = 'create-new-flights')

@app.route('/staff_profile')
def staff_profile():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']

    cursor.close()

    freq_customer, revenue = get_revenue_mostFrequentCustomer(airline_name)
    customer = {'most':freq_customer}

    return render_template('staff_profile.html', username=username,revenue = revenue,customer = customer, section = 'edit-profile-info')

@app.route('/editCustomerProfile',methods=['GET','POST'])
def editCustomerProfile():
    updated_profile = {}
    email_address = session['email_address']
    for key, value in request.form.items():
        if value !='':
            if 'phoneNumbers' in key:  # Handle array-style inputs for phone numbers
                if 'phoneNumbers' not in updated_profile:
                    updated_profile['phoneNumbers'] = []
                updated_profile['phoneNumbers'].append(value)
            else:
                updated_profile[key] = value
    cursor = conn.cursor()
        
    # Example SQL Update: Update relevant fields in the database
    for key, value in updated_profile.items():
        if key != 'phoneNumbers':
            cursor.execute(f'UPDATE customer SET {key} = '+'%s WHERE email_address = %s', (value, email_address))
        else:
            for num in value:
                ins = 'INSERT INTO customer_phone_number VALUES(%s, %s)'
                cursor.execute(ins, (email_address, num))
    conn.commit()
    cursor.close()
    return render_template('customer_profile.html',spending = {}, section = "edit-profile-info")

@app.route('/editStaffProfile',methods=['GET','POST'])
def editStaffProfile():
    updated_profile = {}
    username = session['username']
    for key, value in request.form.items():
        if value !='':
            if 'phoneNumbers' in key:  
                if 'phoneNumbers' not in updated_profile:
                    updated_profile['phoneNumbers'] = []
                updated_profile['phoneNumbers'].append(value)
            elif 'email_address' in key:  
                if 'email_address' not in updated_profile:
                    updated_profile['email_address'] = []
                updated_profile['email_address'].append(value)
            else:
                updated_profile[key] = value
    cursor = conn.cursor()
    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']
    for key, value in updated_profile.items():
        
        if key == 'phoneNumbers':
            for num in value:
                ins = 'INSERT INTO airline_staff_phone_number VALUES(%s, %s)'
                cursor.execute(ins, (username, num))
        elif key == 'email_address':
            for email in value:
                ins_email = 'INSERT INTO airline_staff_email VALUES(%s, %s)'
                cursor.execute(ins_email, (username, email))
        else:
            cursor.execute(f'UPDATE airline_staff SET {key} = '+'%s WHERE username = %s', (value, username))
    conn.commit()
    cursor.close()
    freq_customer, revenue = get_revenue_mostFrequentCustomer(airline_name) 
    customer = {}
    customer['most'] = freq_customer
    return render_template('staff_profile.html',customer = customer,revenue = revenue, section = 'edit-profile-info')

@app.route('/rate_flight',methods=['POST'])
def rateFlight():
    email_address = session['email_address']
    flight_number = request.form['flight_number']
    airline_name = request.form['airline_name']
    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']
    rating = request.form['rating']
    comment = request.form['comment']
    cursor = conn.cursor()   

    query = '''SELECT * FROM rate 
            WHERE email_address = %s AND flight_number = %s AND
                  airline_name = %s AND departure_date = %s AND
                  departure_time = %s'''
    cursor.execute(query, (email_address, flight_number, airline_name, departure_date,
                            departure_time))
    existing_rating = cursor.fetchone()
    if existing_rating:
        return customer_flight("rating error")

    ins = 'INSERT INTO rate VALUES(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (email_address, airline_name, flight_number, departure_time, 
                        departure_date, comment, rating))

    conn.commit()
    cursor.close()

    return customer_flight("rating success")

@app.route('/cancel_flight',methods=['POST'])
def cancelFlight():
    ticket_id = request.form['flight_id']

    cursor = conn.cursor()   

    query = '''SELECT * FROM purchase natural join ticket natural join flight
               WHERE ID = %s AND NOW() >= DATE_SUB(CONCAT(departure_date, ' ', departure_time), INTERVAL 1 DAY)'''
    cursor.execute(query, (ticket_id))
    found = cursor.fetchone()
    if found:
        return customer_flight("cannot cancel")

    query = '''SELECT base_price FROM flight natural join ticket natural join purchase
               WHERE ID = %s'''
    cursor.execute(query, (ticket_id))
    base_price = cursor.fetchone()['base_price']
    conn.commit()

    query = '''UPDATE ticket SET ticket_price = %s 
                        WHERE ID = %s'''
    cursor.execute(query, (base_price, ticket_id))

    ins = 'DELETE FROM purchase WHERE ID =  %s'
    cursor.execute(ins, (ticket_id))

    conn.commit()
    cursor.close()

    return customer_flight("cancel success")

@app.route('/searchFlight',methods=['GET','POST'])
def searchFlight():
    # Get form inputs
    departure_city = request.form['departure_city']
    departure_airport_code = request.form['departure_airport_code']
    arrival_city = request.form['arrival_city']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_date = request.form['departure_date']
    return_date = request.form['return_date']
    if (departure_airport_code ==''and departure_city=='') or (arrival_airport_code==''and arrival_city=='')or(departure_date==''):
        return render_template('index.html',results = {'False':False},section = "search-flights")
    # Prepare the SQL query
    cursor = conn.cursor()
    # Add return date conditionally for round-trip search
    query = """
        SELECT * FROM flight
        WHERE 
            (departure_airport_code in 
                        (SELECT code from airport
                            where city = %s)
                    OR departure_airport_code = %s) 
            AND
            (arrival_airport_code in 
                        (SELECT code from airport
                            where city = %s)
                    OR arrival_airport_code = %s) 
            AND
            departure_date = %s
        """
    params = (departure_city, departure_airport_code, arrival_city, arrival_airport_code, departure_date)

    cursor.execute(query, params)
    flights = cursor.fetchall()
    if return_date:
        return_query = """
        SELECT * FROM flight
        WHERE 
            (departure_airport_code in 
                        (SELECT code from airport
                            where city = %s)
                    OR departure_airport_code = %s) 
            AND
            (arrival_airport_code in 
                        (SELECT code from airport
                            where city = %s)
                    OR arrival_airport_code = %s) 
            AND
            departure_date = %s
        """
        params_return  = (arrival_city, arrival_airport_code,departure_city, departure_airport_code, return_date)
        cursor.execute(return_query, params_return)
        flights_return = cursor.fetchall()
        flights+=flights_return
    

    for flight in flights: 
        query_num_seats = '''SELECT num_seats FROM flight natural join airplane
                   WHERE flight_number = %s'''
        cursor.execute(query_num_seats, (flight['flight_number']))
        num_seats = cursor.fetchone()['num_seats']
        query_purchase_count = '''SELECT COUNT(*) FROM flight natural join purchase natural join ticket 
                                                                    WHERE flight_number = %s'''
        cursor.execute(query_purchase_count, (flight['flight_number']))
        total_purchased = cursor.fetchone()['COUNT(*)']
        if num_seats == total_purchased:
            flight['status'] = "Full"
        elif num_seats * 0.8 <= total_purchased:
            flight['status'] = "Nearly Full"
        else:
            flight['status'] = "Not Full"
            
    results = {'searchFlight':flights}
    cursor.close()
    if 'email_address' in session.keys():
        email_address = session['email_address']
        return render_template('customer_home.html', email_address=email_address, current_date=date.today(), section='search-flights',results = results)
    elif 'username' in session.keys():
        username = session['username']
        return render_template('staff_home.html', username=username, section='search-flights',results = results)
    else:
        return render_template('index.html', section='search-flights',results = results)

@app.route('/flight_status',methods=['GET','POST'])
def flight_status():
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    departure_date = request.form['departure_date']

    cursor = conn.cursor()
    query = """
        SELECT * FROM flight
        WHERE airline_name = %s AND flight_number = %s AND departure_date = %s
    """

    params = (airline_name, flight_number, departure_date)
    cursor.execute(query, params)
    flights = cursor.fetchall()
    results = {'flight_status':flights}
    cursor.close()

    if 'email_address' in session.keys():
        email_address = session['email_address']
        return render_template('customer_home.html', email_address=email_address, section='check-status',results = results)
    elif 'username' in session.keys():
        username = session['username']
        return render_template('staff_home.html', username=username, section='check-status',results = results)
    else:
        return render_template('index.html', section='check-status',results = results)

@app.route('/staff_searchCustomerFlights',methods=['GET','POST'])
def staff_searchCustomerFlights():
    username = session['username']
    email_address = request.form['email_address']

    cursor = conn.cursor()
    query = ''' SELECT * FROM flight natural join purchase natural join ticket
                WHERE airline_name IN (SELECT airline_name FROM airline_staff
                                WHERE username = %s) AND
                email_address = %s
            ''' 

    params = (username, email_address)
    cursor.execute(query, params)
    flights = cursor.fetchall()
    customer = {'customer_flights':flights}

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']
    cursor.close()

    freq_customer, revenue = get_revenue_mostFrequentCustomer(airline_name) 
    customer['most'] = freq_customer

    return render_template('staff_profile.html',section = "view-frequent-customers", queried=True, revenue=revenue , customer = customer)

@app.route('/staff_searchCustomerRates',methods=['GET','POST'])
def staff_searchCustomerRates():
    username = session['username']
    flight_number = request.form['flight_number']
    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']

    cursor = conn.cursor()
    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT * FROM rate
               WHERE airline_name = %s AND flight_number = %s AND departure_date = %s AND departure_time = %s'''
    params = (airline_name, flight_number, departure_date, departure_time)
    cursor.execute(query, params)
    rates = cursor.fetchall()
  
    query = '''SELECT AVG(rating) FROM rate
               WHERE airline_name = %s AND flight_number = %s AND departure_date = %s AND departure_time = %s'''
    params = (airline_name, flight_number, departure_date, departure_time)
    cursor.execute(query, params)
    avg_rating = cursor.fetchone()['AVG(rating)']
    cursor.close()

    freq_customer, revenue = get_revenue_mostFrequentCustomer(airline_name)
    customer = {"most":freq_customer}

    return render_template('staff_profile.html',section = "view-flight-rates", queried=True, avg_rating=avg_rating, rates=rates, revenue=revenue , customer = customer)

def get_revenue_mostFrequentCustomer(airline_name):
    username = session['username']

    cursor = conn.cursor()
    query = ''' SELECT email_address, SUM(ticket_price) as revenue
                FROM flight natural join purchase natural join ticket
                WHERE airline_name = %s
                GROUP BY email_address
                ORDER BY revenue DESC
            ''' 

    params = (airline_name)
    cursor.execute(query, params)
    user = cursor.fetchone()
    customer = user['email_address']
    revenue = user['revenue']
    return customer, revenue

@app.route('/customer_flight')
def customer_flight(error="none"):
    email_address = session['email_address']

    cursor = conn.cursor()
    query = """
        SELECT * FROM purchase natural join ticket natural join flight
        WHERE 
            (email_address = %s) AND (departure_date < CURDATE() OR
                                        (departure_date = CURDATE() AND
                                            departure_time < CURTIME()))
    """
    params = (email_address)

    cursor.execute(query, params)
    previous_flights = cursor.fetchall()
    results = {'previousFlights':previous_flights}

    query = """
        SELECT * FROM purchase natural join ticket natural join flight
        WHERE 
            (email_address = %s) AND (departure_date > CURDATE() OR
                                        (departure_date = CURDATE() AND
                                            departure_time > CURTIME()))
    """
    params = (email_address)

    cursor.execute(query, params)
    upcoming_flights = cursor.fetchall()
    results['upcomingFlights'] = upcoming_flights

    return render_template('customer_flight.html',results = results, error=error)

@app.route('/default_customer_spending')
def default_customer_spending():
    email_address = session['email_address']

    cursor = conn.cursor()

    query = '''SELECT ROUND(SUM(ticket_price), 2) as total FROM purchase natural join ticket
               WHERE email_address = %s AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)'''

    params = (email_address)
    cursor.execute(query, params)
    total_spending = cursor.fetchone()['total']
    if not total_spending:
        total_spending = 0.00

    query = '''SELECT DATE_FORMAT(purchase_date, '%%M') AS month, ROUND(SUM(ticket_price), 2) AS total_spent
               FROM purchase natural join ticket
               WHERE email_address = %s AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
               GROUP BY month
               ORDER BY month'''
    params = (email_address)
    cursor.execute(query, params)
    spending_months = cursor.fetchall()

    spending = {"total_spending":total_spending, "spending_months":spending_months}

    cursor.close()

    return render_template('customer_profile.html',spending=spending,day_range_spending =False,section = 'track-spending')

@app.route('/range_customer_spending',methods=['GET','POST'])
def range_customer_spending():
    email_address = session['email_address']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    cursor = conn.cursor()

    query = '''SELECT ROUND(SUM(ticket_price), 2) as total FROM purchase natural join ticket
               WHERE email_address = %s AND purchase_date >= %s AND purchase_date <= %s'''

    params = (email_address, start_date, end_date)
    cursor.execute(query, params)
    total_spending = cursor.fetchone()['total']
    if not total_spending:
        total_spending = 0.00

    query = '''SELECT DATE_FORMAT(purchase_date, '%%M') AS month, ROUND(SUM(ticket_price), 2) AS total_spent
               FROM purchase natural join ticket
               WHERE email_address = %s AND purchase_date >= %s AND purchase_date <= %s
               GROUP BY month
               ORDER BY month'''
    params = (email_address, start_date, end_date)
    cursor.execute(query, params)
    spending_months = cursor.fetchall()

    spending = {"total_spending":total_spending, "spending_months":spending_months}

    cursor.close()

    return render_template('customer_profile.html',spending=spending,day_range_spending =True,section = 'track-spending')

@app.route('/customer_profile')
def customer_profile():
    return render_template('customer_profile.html', section = 'edit-profile-info')

@app.route('/createNewFlights',methods=['GET','POST'])
def createNewFlights():
    username = session['username']
    flight_number = request.form['flight_number']
    departure_time = request.form['departure_time']
    departure_date = request.form['departure_date']
    arrival_date = request.form['arrival_date']
    arrival_time = request.form['arrival_time']
    flight_status = request.form['flight_status']
    base_price = request.form['base_price']
    departure_airport_code = request.form['departure_airport_code']
    arrival_airport_code = request.form['arrival_airport_code']
    airplane_id = request.form['airplane_id']

    cursor = conn.cursor()   

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)
    airline_name = cursor.fetchone()['airline_name']

    departure_date_time = departure_date + " " + departure_time
    arrival_date_time = arrival_date + " " + arrival_time

    query = '''
            SELECT * 
            FROM maintenance_procedure 
            WHERE airplane_id = %s 
            AND (
                EXISTS (
                    SELECT 1 
                    FROM maintenance_procedure AS mp
                    WHERE mp.airplane_id = %s 
                        AND %s BETWEEN CONCAT(mp.maintenance_start_date, ' ', mp.maintenance_start_time)
                                    AND CONCAT(mp.maintenance_end_date, ' ', mp.maintenance_end_time)
                )
                OR EXISTS (
                    SELECT 1 
                    FROM maintenance_procedure AS mp
                    WHERE mp.airplane_id = %s 
                        AND %s BETWEEN CONCAT(mp.maintenance_start_date, ' ', mp.maintenance_start_time)
                                    AND CONCAT(mp.maintenance_end_date, ' ', mp.maintenance_end_time)
                )
                OR EXISTS (
                    SELECT 1 
                    FROM maintenance_procedure AS mp
                    WHERE mp.airplane_id = %s 
                        AND %s < CONCAT(mp.maintenance_end_date, ' ', mp.maintenance_end_time)
                        AND %s > CONCAT(mp.maintenance_start_date, ' ', mp.maintenance_start_time)
                )
            )
            '''
    cursor.execute(query, (airplane_id, airplane_id, departure_date_time, 
                                airplane_id, arrival_date_time, airplane_id, 
                                arrival_date_time, departure_date_time))
    being_maintained = cursor.fetchone()

    if (being_maintained):
        return render_template('staff_manage.html',section = 'create-new-flights',error="maintenance")

    ins = 'INSERT INTO flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (airline_name, flight_number, departure_time, departure_date, 
                        arrival_date, arrival_time, base_price, flight_status,
                        departure_airport_code, arrival_airport_code, airplane_id))

    query = '''SELECT num_seats FROM airplane
               WHERE airplane_id = %s'''
    cursor.execute(query, (airplane_id))
    num_seats = cursor.fetchone()['num_seats']

    last_ticket_id_query = 'SELECT MAX(ID) FROM ticket'  
    cursor.execute(last_ticket_id_query)

    last_ticket_id_result = cursor.fetchone()['MAX(ID)']
    new_ticket_id = (int(last_ticket_id_result) + 1) if last_ticket_id_result else 1

    for i in range(new_ticket_id, new_ticket_id + num_seats):
        ins = 'INSERT INTO ticket VALUES(%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (i, base_price, airline_name, flight_number, 
                        departure_time, departure_date))

    conn.commit()
    cursor.close()

    return render_template('staff_manage.html',section = 'create-new-flights',error="none")

@app.route('/changeFlightStatus',methods=['GET','POST'])
def changeFlightStatus():
    username = session['username']
    flight_number = request.form['flight_number']
    flight_status = request.form['flight_status']
    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']

    cursor = conn.cursor()   

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)

    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT * FROM flight 
               WHERE flight_number = %s AND departure_date = %s AND departure_time = %s AND airline_name = %s'''
    cursor.execute(query, (flight_number, departure_date, departure_time,airline_name))  
    flights = cursor.fetchall()

    if not flights:
        return render_template('staff_manage.html',section = 'change-flight-status',error ="no flights")
    
    ins = '''UPDATE flight SET flight_status = %s 
             WHERE flight_number = %s AND departure_date = %s AND departure_time = %s AND airline_name = %s '''
    cursor.execute(ins, (flight_status, flight_number, departure_date, departure_time,airline_name))

    conn.commit()
    cursor.close()

    return render_template('staff_manage.html',section = 'change-flight-status',error="no error")

@app.route('/addAirplane',methods=['GET','POST'])
def addAirplane():
    username = session['username']
    #airline_name = request.form['airline_name']
    airplane_id = request.form['airplane_id']
    num_seats = request.form['capacity']
    manufacturing_company = request.form['manufacturing_company']
    model_num = request.form['airplane_model']
    manufacturing_date = request.form['manufacturing_date']
    age = 0
    
    error = False
    cursor = conn.cursor()   

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)

    airline_name = cursor.fetchone()['airline_name']


    ins = 'INSERT INTO airplane VALUES(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (airline_name, airplane_id, num_seats, manufacturing_company, 
                        model_num, manufacturing_date, age))

    update_age_query = '''
        UPDATE airplane
        SET age = TIMESTAMPDIFF(YEAR, manufacturing_date, CURDATE()) 
                - (CURDATE() < DATE_ADD(manufacturing_date, INTERVAL TIMESTAMPDIFF(YEAR, manufacturing_date, CURDATE()) YEAR))
        WHERE airplane_id = %s;
        '''

    cursor.execute(update_age_query, (airplane_id,))

    conn.commit()

    query = ''' SELECT * FROM airplane
                                WHERE airline_name = %s'''
    params = (airline_name)
    cursor.execute(query, params)

    airplanes = cursor.fetchall()

    cursor.close()

    return render_template('staff_manage.html',section = 'add-airplane', airplanes=airplanes, error=error)

@app.route('/addAirport',methods=['GET','POST'])
def addAirport():
    code = request.form['airport_code']
    name = request.form['airport_name']
    num_terminals = request.form['num_terminals']
    city = request.form['city']
    country = request.form['country']
    airport_type = request.form['airport_type']

    cursor = conn.cursor()   

    ins = 'INSERT INTO airport VALUES(%s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (code, name, city, country, num_terminals, airport_type))

    conn.commit()
    cursor.close()
    
    return render_template('staff_manage.html',section = 'add-airport')

@app.route('/scheduleMaintenance',methods=['GET','POST'])
def scheduleMaintenance():
    cursor = conn.cursor()  
    username = session['username']
    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''
    params = (username)
    cursor.execute(query, params)

    staff_airline_name = cursor.fetchone()['airline_name']
    airline_name = staff_airline_name
    airplane_id = request.form['airplane_id']

    maintenance_start_date = request.form['maintenance_start_date']
    maintenance_start_time = request.form['maintenance_start_time']
    maintenance_end_date = request.form['maintenance_end_date']
    maintenance_end_time = request.form['maintenance_end_time']

    ins = 'INSERT INTO maintenance_procedure VALUES(%s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (airline_name, airplane_id, maintenance_start_time,
                        maintenance_start_date, maintenance_end_time, maintenance_end_date))

    conn.commit()
    cursor.close()

    return render_template('staff_manage.html',section = 'schedule-maintenance')

@app.route('/staff_view_flights_default',methods=['GET','POST'])
def staff_view_flights_default():
    username = session['username']

    cursor = conn.cursor()

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''

    cursor.execute(query, (username,))
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT * FROM flight
               WHERE airline_name = %s AND departure_date BETWEEN CURDATE()
                                                                  AND
                                                                  DATE_ADD(CURDATE(), INTERVAL 1 MONTH)'''
    cursor.execute(query, (airline_name))
    flights = cursor.fetchall()

    results = {"flights":flights}
    cursor.close()
    
    return render_template('staff_home.html',section = 'view-flights', ranged=False, username = username,results = results)

@app.route('/staff_view_flights_ranged',methods=['GET','POST'])
def staff_view_flights_ranged():
    username = session['username']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    departure_airport_code = request.form['departure_airport_code']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_airport_city = request.form['departure_airport_city']
    arrival_airport_city = request.form['arrival_airport_city']

    if not start_date and not end_date and not departure_airport_code and not departure_airport_city and not arrival_airport_code and arrival_airport_city:
        return render_template('staff_home.html',section = 'view-flights', error="no input")
    cursor = conn.cursor()

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''

    cursor.execute(query, (username,))
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT DISTINCT airline_name, flight_number, departure_date, departure_time,
                               arrival_date, arrival_time, base_price, flight_status, airplane_id
               FROM flight natural join airport
               WHERE airline_name = %s'''
    
    params = (airline_name,)

    if start_date:
        query += 'AND departure_date >= %s'
        params += (start_date,)
    if end_date:
        query += 'AND departure_date <= %s'
        params += (end_date,)
    if departure_airport_code:
        query += 'AND departure_airport_code = %s'
        params += (departure_airport_code,)
    if arrival_airport_code:
        query += 'AND arrival_airport_code >= %s'
        params += (arrival_airport_code,)
    if departure_airport_city:
        query += '''AND (departure_airport_code in 
                        (SELECT code from airport
                            where city = %s))'''
        params += (departure_airport_city,)
    if arrival_airport_city:
        query += '''AND (arrival_airport_code in 
                        (SELECT code from airport
                            where city = %s))'''
        params += (arrival_airport_city,)

    cursor.execute(query, params)
    flights = cursor.fetchall()

    for flight in flights:
        print(flight)

    results = {"flights":flights}
    cursor.close()
    
    return render_template('staff_home.html',section = 'view-flights', ranged=True, username = username,results = results)


@app.route('/staff_view_customer',methods=['GET','POST'])
def staff_view_customer():
    username = session['username']
    flight_number = request.form['flight_number']
    departure_date = request.form['departure_date']

    cursor = conn.cursor()

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''

    cursor.execute(query, (username,))
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT * FROM flight natural join ticket natural join purchase
               WHERE airline_name = %s AND flight_number = %s 
               AND departure_date = %s'''
    cursor.execute(query, (airline_name, flight_number, departure_date))
    customers = cursor.fetchall()

    results = {"customers":customers}
    cursor.close()
    
    return render_template('staff_home.html',section = 'view-customers',username = username,results = results)


@app.route('/staff_view_delayed_ontime',methods=['GET','POST'])
def staff_view_delayed_ontime():
    username = session['username']

    cursor = conn.cursor()

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''

    cursor.execute(query, (username,))
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT * FROM flight 
               WHERE airline_name = %s AND flight_status = %s'''
    cursor.execute(query, (airline_name, "Delayed"))
    delayed_flights = cursor.fetchall()

    results = {"delayedFlights":delayed_flights}

    query = '''SELECT * FROM flight 
               WHERE airline_name = %s AND flight_status = %s'''
    cursor.execute(query, (airline_name, "On-Time"))
    ontime_flights = cursor.fetchall()

    results["ontimeFlights"] = ontime_flights
    cursor.close()
    
    return render_template('staff_home.html',section = 'view-delayed-ontime',username = username,results = results)

@app.route('/staff_view_earned_revenue',methods=['GET','POST'])
def staff_view_earned_revenue():
    username = session['username']

    cursor = conn.cursor()

    query = ''' SELECT airline_name FROM airline_staff
                                WHERE username = %s'''

    cursor.execute(query, (username,))
    airline_name = cursor.fetchone()['airline_name']

    query = '''SELECT ROUND(SUM(ticket_price), 2) FROM purchase natural join ticket 
               WHERE airline_name = %s AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'''
    cursor.execute(query, (airline_name))
    revenue_past_month = cursor.fetchone()['ROUND(SUM(ticket_price), 2)']

    if not revenue_past_month:
        revenue_past_month = 0

    query = '''SELECT ROUND(SUM(ticket_price), 2) FROM purchase natural join ticket 
               WHERE airline_name = %s AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)'''
    cursor.execute(query, (airline_name))
    revenue_past_year = cursor.fetchone()['ROUND(SUM(ticket_price), 2)']

    if not revenue_past_year:
        revenue_past_year = 0

    query = '''SELECT DATE_FORMAT(purchase_date, '%%M') AS month, COUNT(*) as ticket_count
               FROM purchase natural join ticket natural join flight
               WHERE airline_name = %s AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
               GROUP BY month
               ORDER BY month'''
    cursor.execute(query, (airline_name))
    spending_months = cursor.fetchall()

    revenue = {"last_year":revenue_past_year, "last_month":revenue_past_month, "ticket_count":spending_months}

    cursor.close()

    customer, ret = get_revenue_mostFrequentCustomer(airline_name)
    return render_template('staff_profile.html', customer = customer, section='view-earned-revenue', revenue = revenue)

@app.route('/purchase_flights',methods=['GET','POST'])
def purchaseFlights():
    flight_number = request.form['flight_number']
    airline_name = request.form['airline_name']

    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']

    base_price = request.form['base_price']

    ticket_user_first_name = request.form['ticket_user_first_name']
    ticket_user_last_name = request.form['ticket_user_last_name']
    ticket_user_date_of_birth = request.form['ticket_user_date_of_birth']

    card_type = request.form['card_type']
    card_number = request.form['card_number']
    card_name = request.form['card_name']
    expiration_date = request.form['expiration_date']

    capacity_status = request.form['capacity_status']

    cursor = conn.cursor()

    query = '''SELECT ID FROM ticket
               WHERE flight_number = %s AND airline_name = %s AND
               departure_date = %s AND departure_time = %s'''
    cursor.execute(query, (flight_number, airline_name, departure_date, departure_time))
    tickets = cursor.fetchall()

    purchased = False
    for ticket in tickets:
        if_purchased = '''SELECT * FROM purchase
                          WHERE ID = %s'''
        cursor.execute(if_purchased, (ticket['ID']))
        ticket_id = cursor.fetchone()

        if not ticket_id:
            if capacity_status == "Nearly Full":
                query = '''UPDATE ticket SET ticket_price = %s 
                        WHERE ID = %s'''
                cursor.execute(query, (float(base_price) * 1.25, ticket['ID']))
                conn.commit()
                
            ins = 'INSERT INTO purchase VALUES(%s, %s, %s, %s, %s, NOW(), NOW(), %s, %s, %s, %s)'
            cursor.execute(ins, (session['email_address'], ticket['ID'], ticket_user_first_name, 
                            ticket_user_last_name, ticket_user_date_of_birth, card_type, card_number, 
                            card_name, expiration_date))
            purchased = True
            break

    if not purchased:
        return render_template('customer_home.html',section = 'search-flights')

    conn.commit()
    cursor.close()
    
    return customer_home()

@app.route('/logout_customer')
def logout_customer():
    session.pop('email_address')
    return redirect('/')

@app.route('/logout_staff')
def logout_staff():
    session.pop('username')
    return redirect('/')
        
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
