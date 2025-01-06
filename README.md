Here's a simplified `README.md` focused only on the login and registration features for your Flask project:

---

# Flask User Authentication (Login & Register)

This project is a simple user authentication system built using **Flask**, **WTForms**, **MySQL**, and **bcrypt** for password hashing. It allows users to register, log in, and includes basic validation and aesthetic form styling.

## Features

- **User Registration**: Users can sign up by providing their name, email, and password.
- **User Login**: Users can log in using their email and password.
- **Flash Messages**: Display success or error messages after registration or login.
- **Aesthetic Forms**: Forms are styled using Bootstrap and custom CSS for an improved user experience.

## Technologies Used

- **Flask**: Python web framework for building the application.
- **WTForms**: For handling form submissions and validation.
- **bcrypt**: For securely hashing passwords.
- **MySQL**: Database to store user information.
- **Bootstrap**: Front-end framework used for responsive design and styling.

---

## Prerequisites

To run this project, you will need:

- **Python 3.x** installed on your machine.
- **MySQL** installed and running.
- **MySQL Workbench** (optional, but helpful for managing your database).

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-user-auth.git
cd flask-user-auth
```

### 2. Install Python Dependencies

Create a virtual environment (optional but recommended) and install the required dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Set Up the MySQL Database

1. Open your MySQL shell or MySQL Workbench.
2. Create a new database:

```sql
CREATE DATABASE mydatabase;
```

3. Create the `users` table:

```sql
USE mydatabase;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

4. Update your `app.py` file with your MySQL credentials (if necessary).

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Your MySQL password
app.config['MYSQL_DB'] = 'mydatabase'  # Your MySQL database name
```

### 4. Run the Application

To start the Flask application, run:

```bash
python app.py
```

This will start the Flask development server, usually running on `http://localhost:5000/`.

---

## Usage

### 1. Home Page (`/`)

Visit the homepage at [http://localhost:5000/](http://localhost:5000/) to see the main landing page.

### 2. Register Page (`/register`)

- Visit [http://localhost:5000/register](http://localhost:5000/register) to register a new user.
- Fill in the form with your **Name**, **Email**, and **Password**.

### 3. Login Page (`/login`)

- Visit [http://localhost:5000/login](http://localhost:5000/login) to log in with your registered email and password.

---

## Flash Messages

Flash messages are displayed to inform users of success or failure after actions like registration or login. They appear above the forms and provide user feedback (e.g., success or error messages).

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Notes:

- Make sure you replace the `localhost` in the URLs with the actual URL if you deploy the app online.
- The project can be extended to include more features such as a user dashboard, user logout, and password reset functionality.

---

This version of the `README.md` focuses only on the login and registration features, making it simpler and to the point.