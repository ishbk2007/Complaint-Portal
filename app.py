from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_url_path='/static')

# Configure Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='snacompreg@gmail.com',
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),  # Get from environment variable
    SECRET_KEY=os.environ.get('SECRET_KEY', 'your-secret-key-here')
)

mail = Mail(app)
RECIPIENT_EMAIL = 'ishbk2007@gmail.com'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        complaint = request.form.get('complaint')
        
        if not app.config['MAIL_PASSWORD']:
            print("Error: MAIL_PASSWORD environment variable is not set")
            flash('Email configuration is missing! Please contact the administrator. 📧', 'error')
            return redirect(url_for('index'))
        
        try:
            msg = Message(
                subject='New Complaint Received',
                sender=app.config['MAIL_USERNAME'],
                recipients=[RECIPIENT_EMAIL],
                body=f'''
                New Complaint Received!
                
                Complaint:
                {complaint}
                '''
            )
            mail.send(msg)
            flash('Thank you! Your complaint has been registered and sent! 🌟', 'success')
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            flash(f'Oops! Something went wrong: {str(e)}. Please try again! 😢', 'error')
            
        return redirect(url_for('index'))
        
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 