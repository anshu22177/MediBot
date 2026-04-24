# Medibot - Medical Symptom Guidance Chatbot

A web-based medical symptom guidance chatbot built with Python Flask, HTML, CSS, and JavaScript. This application provides educational information about common symptoms and is designed for educational purposes only.

## ⚠️ Important Medical Disclaimer

**This application does NOT:**
- Provide medical diagnoses
- Prescribe medications
- Replace professional medical advice

**This application DOES:**
- Provide educational information about symptoms
- Offer general care advice
- Suggest when to consult a healthcare provider

Always consult with a qualified healthcare provider for proper evaluation, diagnosis, and treatment. In case of a medical emergency, call emergency services immediately.

## Features

- **User Authentication**: Secure signup and login with password hashing
- **Session Management**: Session-based authentication for secure access
- **Symptom Guidance**: Rule-based system for common symptoms:
  - Fever
  - Cold and cough
  - Headache
  - Stomach pain
  - Fatigue
- **Chat History**: Stores conversation history per user
- **Responsive Design**: Works on desktop and mobile devices
- **Medical Safety**: Clear disclaimers and educational-only information

## Project Structure

```
Medibot/
│
├── app.py                 # Main Flask application
├── chatbot.py             # Rule-based symptom guidance logic
├── requirements.txt       # Python dependencies
├── medibot.db            # SQLite database (created on first run)
│
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── login.html       # Login page
│   ├── signup.html      # Signup page
│   └── chatbot.html     # Chatbot interface
│
└── static/              # Static files
    ├── css/
    │   └── style.css    # Main stylesheet
    └── js/
        └── chatbot.js   # Chatbot JavaScript
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

Navigate to the project directory:
```bash
cd Medibot
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 5: Access the Application

1. Open your web browser
2. Navigate to `http://localhost:5000`
3. You'll be redirected to the login page
4. Create a new account or login with existing credentials

## Usage

1. **Sign Up**: Create a new account with your name, email, and password
2. **Login**: Use your credentials to access the chatbot
3. **Chat**: Describe your symptoms in the chat interface
4. **Get Guidance**: Receive educational information about possible causes, care advice, and when to consult a doctor
5. **Logout**: Click the logout button when done

## Example Queries

- "I have a fever and headache"
- "I'm experiencing stomach pain and nausea"
- "I have a persistent cough"
- "I feel very tired and weak"

## Database

The application uses SQLite database (`medibot.db`) to store:
- User accounts (name, email, hashed passwords)
- Chat history (user messages and bot responses)

The database is automatically created on first run.

## Security Features

- Password hashing using Werkzeug's security functions
- Session-based authentication
- SQL injection protection (using parameterized queries)
- Secure password requirements (minimum 6 characters)

## Development Notes

### Changing the Secret Key

For production use, change the `secret_key` in `app.py`:
```python
app.secret_key = 'your-secret-key-change-in-production'
```

### Adding New Symptoms

To add support for new symptoms, edit `chatbot.py` and add new condition checks in the `get_symptom_guidance()` function.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, modify the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

### Database Issues

If you encounter database errors, delete `medibot.db` and restart the application. The database will be recreated automatically.

### Module Not Found Errors

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Security**: Werkzeug (password hashing)

## License

This project is for educational purposes only.

## Support

For issues or questions, please refer to the code comments or create an issue in the project repository.

---

**Remember**: This is an educational tool. Always consult healthcare professionals for medical advice.


