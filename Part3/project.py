#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect,send_file
import pymysql.cursors
import os
#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='root',
                        password='',
                        db='Airline',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

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

#Authenticates the login
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
        return redirect(url_for('home'))
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
        conn.commit()
        cursor.close()
        return render_template('index.html')
    

@app.route('/images/<path:filename>')
def get_image(filename):
    try:
        # Specify your image directory path
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
    
    email_address = session['email_address']
    cursor = conn.cursor()
    query = 'SELECT first_name, last_name FROM airline_staff WHERE email_address = %s'
    cursor.execute(query, (email_address))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['first_name'] + " " + each['last_name'])
    cursor.close()
    return render_template('staff_home.html', email_address=email_address, posts=data1)


@app.route('/logout')
def logout():
    session.pop('email_address')
    return redirect('/')
        
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
