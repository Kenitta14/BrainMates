import sqlite3
from werkzeug.security import generate_password_hash

# Connect to SQLite database
conn = sqlite3.connect('brainmates.db')
cursor = conn.cursor()

# Create User table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    subject TEXT NOT NULL,
    available_time TEXT NOT NULL,
    preferred_place TEXT NOT NULL,
    study_style TEXT NOT NULL
)
''')

# Sample user data
users = [
    {
        'name': 'Alice Johnson',
        'email': 'alice@example.com',
        'password': generate_password_hash('password123'),
        'subject': 'Computer Science',
        'available_time': 'Evening',
        'preferred_place': 'Library',
        'study_style': 'Group'
    },
    {
        'name': 'Bob Smith',
        'email': 'bob@example.com',
        'password': generate_password_hash('password456'),
        'subject': 'Math',
        'available_time': 'Afternoon',
        'preferred_place': 'Cafe',
        'study_style': 'Individual'
    },
    {
        'name': 'Charlie Brown',
        'email': 'charlie@example.com',
        'password': generate_password_hash('password789'),
        'subject': 'Science',
        'available_time': 'Morning',
        'preferred_place': 'Online',
        'study_style': 'Group'
    }
]

# Insert users
for user in users:
    cursor.execute('''
    INSERT INTO user (name, email, password, subject, available_time, preferred_place, study_style)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        user['name'], 
        user['email'], 
        user['password'], 
        user['subject'], 
        user['available_time'], 
        user['preferred_place'], 
        user['study_style']
    ))

# Commit changes and close connection
conn.commit()
conn.close()

print("SQLite database created with sample users.")