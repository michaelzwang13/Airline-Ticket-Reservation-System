#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect,send_file
import pymysql.cursors
import os
import sys
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
                        password='',#
                        db='Airline',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html',section = "search-flights") # set default to search flights

@app.route('/index_searchflights')
def index_searchflights():
    return render_template('index.html',section = "search-flights")

@app.route('/index_checkstatus')
def index_checkstatus():
    return render_template('index.html',section = "check-status")

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
    query = 'SELECT * FROM customer WHERE email_address = %s and password = %s'
    cursor.execute(query, (email_address, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['email_address'] = email_address
        return redirect(url_for('customer_home'))
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
    query = 'SELECT * FROM airline_staff WHERE username = %s and password = %s'
    cursor.execute(query, (username, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['username'] = username
        return redirect(url_for('staff_home'))
    else:
        #returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('staff_login.html', error=error)

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
        cursor.execute(ins, (email_address, password, first_name, last_name, building_name,
                            street_name, apt_num, city, state, zipcode, date_of_birth,
                            passport_number, passport_expiration, passport_country))
        ins_phone = 'INSERT INTO customer_phone_number VALUES(%s, %s)'
        for num in phone_number:
            cursor.execute(ins_phone, (email_address,num))
        conn.commit()
        cursor.close()
        return render_template('customer_home.html')

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
        cursor.execute(ins, (username, airline_name, password, first_name, last_name, date_of_birth))
        ins_phone = 'INSERT INTO airline_staff_phone_number VALUES(%s, %s)'
        for num in phone_number:
            cursor.execute(ins_phone, (username,num))
        ins_email = 'INSERT INTO airline_staff_email VALUES(%s, %s)'
        for email in email_address:
            cursor.execute(ins_email, (username,email))
        conn.commit()
        cursor.close()
        return render_template('staff_home.html')
    

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
    for each in data1:
        print(each['first_name'] + " " + each['last_name'])
    cursor.close()
    
    return render_template('customer_home.html', email_address=email_address, posts=data1)

@app.route('/staff_home')
def staff_home():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['first_name'] + " " + each['last_name'])
    cursor.close()
    return render_template('staff_home.html', username=username, posts=data1)

@app.route('/staff_manage')
def staff_manage():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['first_name'] + " " + each['last_name'])
    cursor.close()
    return render_template('staff_manage.html', username=username, posts=data1)

@app.route('/staff_profile')
def staff_profile():
    username = session['username']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['first_name'] + " " + each['last_name'])
    cursor.close()
    return render_template('staff_profile.html', username=username, posts=data1)

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
    return render_template('customer_profile.html')

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
            cursor.execute(f'UPDATE customer SET {key} = '+'%s WHERE username = %s', (value, username))
    conn.commit()
    cursor.close()
    return render_template('staff_profile.html')

@app.route('/searchFlight',methods=['GET','POST'])
def searchFlight():
    # Get form inputs
    departure_city = request.form['departure_city']
    departure_airport_code = request.form['departure_airport_code']
    arrival_city = request.form['arrival_city']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_date = request.form['departure_date']
    return_date = request.form['return_date']

    # Prepare the SQL query
    cursor = conn.cursor()
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
    
    # Add return date conditionally for round-trip search
    if return_date:
        query += " AND return_date = %s"
        params += (return_date,)

    cursor.execute(query, params)
    flights = cursor.fetchall()
    results = {'searchFlight':flights}
    cursor.close()

    return render_template('index.html',results = results,section = "search-flights")

@app.route('/flight_status',methods=['GET','POST'])
def flight_status():
    status = {"status":"On-Time","flight_number":"123"}
    results = {'flightStatus':status}
    return render_template('index.html',results = results,section = "check-status")

@app.route('/customer_flight')
def customer_flight():
    return render_template('customer_flight.html')

@app.route('/customer_profile')
def customer_profile():
    return render_template('customer_profile.html')


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
