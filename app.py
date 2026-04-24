"""
Medibot - Medical Symptom Guidance Chatbot
Main Flask application file
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime
from chatbot import get_symptom_guidance

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Change this in production!

# Database file path
DATABASE = 'medibot.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with required tables"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Chat history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on first run
if not os.path.exists(DATABASE):
    init_db()

def require_login(f):
    """Decorator to require user login"""
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def index():
    """Redirect to login if not logged in, else to chatbot"""
    if 'user_id' in session:
        return redirect(url_for('chatbot'))
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User registration page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not name or not email or not password:
            return render_template('signup.html', error='All fields are required')
        
        if len(password) < 6:
            return render_template('signup.html', error='Password must be at least 6 characters')
        
        conn = get_db()
        cursor = conn.cursor()
        
        # Check if email already exists
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        if cursor.fetchone():
            conn.close()
            return render_template('signup.html', error='Email already registered')
        
        # Hash password and insert user
        hashed_password = generate_password_hash(password)
        cursor.execute(
            'INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
            (name, email, hashed_password)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            return render_template('login.html', error='Email and password are required')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('chatbot'))
        else:
            return render_template('login.html', error='Invalid email or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout user and clear session"""
    session.clear()
    return redirect(url_for('login'))

@app.route('/chatbot')
@require_login
def chatbot():
    """Main chatbot page - only accessible when logged in"""
    return render_template('chatbot.html', user_name=session.get('user_name', 'User'))

@app.route('/api/chat', methods=['POST'])
@require_login
def chat():
    """API endpoint for chatbot interactions"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    
    # Get symptom guidance from chatbot module
    bot_response = get_symptom_guidance(user_message)
    
    # Store chat history
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO chat_history (user_id, user_message, bot_response) VALUES (?, ?, ?)',
        (session['user_id'], user_message, bot_response)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'response': bot_response})

@app.route('/api/history')
@require_login
def get_history():
    """Get chat history for the logged-in user"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT user_message, bot_response, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT 50',
        (session['user_id'],)
    )
    history = cursor.fetchall()
    conn.close()
    
    return jsonify([{
        'user_message': row['user_message'],
        'bot_response': row['bot_response'],
        'timestamp': row['timestamp']
    } for row in history])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


