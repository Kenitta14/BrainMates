from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Construct full path to the database
db_path = os.path.join('D:/brainmates/', 'brainmates.db')

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    available_time = db.Column(db.String(50), nullable=False)
    preferred_place = db.Column(db.String(100), nullable=False)
    study_style = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    return jsonify({"message": "BrainMates Backend is Running"}), 200


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not all(key in data for key in ['name', 'email', 'password', 'subject', 'available_time', 'preferred_place', 'study_style']):
        return jsonify({"error": "Missing fields"}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        subject=data['subject'],
        available_time=data['available_time'],
        preferred_place=data['preferred_place'],
        study_style=data['study_style']
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Registration failed: {str(e)}"}), 500


@app.route('/find_buddies', methods=['GET'])
def find_buddies():
    subject = request.args.get('subject', None)
    available_time = request.args.get('available_time', None)
    preferred_place = request.args.get('preferred_place', None)

    query = User.query

    if subject and subject != 'All Subjects':
        query = query.filter(User.subject == subject)
    if available_time and available_time != 'All Times':
        query = query.filter(User.available_time == available_time)
    if preferred_place and preferred_place != 'All Places':
        query = query.filter(User.preferred_place == preferred_place)

    buddies = query.all()

    return jsonify([{
        'name': buddy.name,
        'subject': buddy.subject,
        'available_time': buddy.available_time,
        'preferred_place': buddy.preferred_place,
        'study_style': buddy.study_style
    } for buddy in buddies]), 200


if __name__ == '__main__':
    # Ensure the directory exists
    os.makedirs('D:/brainmates', exist_ok=True)

    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=5000)
