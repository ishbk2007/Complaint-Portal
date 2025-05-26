# Cute Complaint Registration Portal 🌸

A beautiful and user-friendly web application for registering complaints that automatically sends them to a designated email address.

## Features ✨

- Beautiful, modern UI with a cute design
- Easy-to-use complaint form
- Email notification system
- Form validation
- Success/error notifications
- Mobile-responsive design

## Setup 🚀

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with the following content:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
RECIPIENT_EMAIL=destination@example.com
```

Note: For Gmail, you'll need to:
1. Enable 2-factor authentication
2. Generate an App Password (Google Account → Security → App Passwords)
3. Use that App Password in the .env file

## Running the Application 🌟

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Technologies Used 💻

- Python Flask
- Flask-Mail
- HTML/CSS
- Google Fonts (Nunito) 