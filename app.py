from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:King001@@localhost/Ekart'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'anand321'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(60), nullable=False)

with app.app_context():
    db.create_all()

# Rest of your code...


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(full_name=full_name, username=username, email=email, phone=phone, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            # Perform login actions (e.g., set a session variable)
            return redirect(url_for('home'))  # Replace 'home' with the correct endpoint
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
