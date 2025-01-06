from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import bcrypt
from flask_mysqldb import MySQL

# Initialize Flask application
app = Flask(__name__)

# Configuration for MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Add your MySQL password here if set
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = 'your_secret_key_here'

# Initialize MySQL connection
mysql = MySQL(app)

# Registration Form
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (field.data,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError('Email is already taken')

# Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Home Page Route
@app.route('/')
def index():
    return render_template('index.html')

# Registration Page Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        # Hashing the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert new user into the database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                       (name, email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        # Redirect to login page after successful registration
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# Login Page Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if the user exists in the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        # Validate user login
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Please check your email and password.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

# Dashboard Route (Optional: can be used after a successful login)
@app.route('/dashboard')
def dashboard():
    # Add logic to display user dashboard here
    return render_template('dashboard.html')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
