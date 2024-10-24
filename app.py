from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'saksamtechnologies@tenkasi627808'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = ('SakSam Technologies', 'your_email@gmail.com')

# Initialize Flask-Mail
mail = Mail(app)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home_redirect():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route to handle form submission
@app.route('/send/contact', methods=['POST'])
def send_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Name, Email, and Message are required fields.', 'error')
        return redirect(url_for('contact'))

    try:
        msg = Message(f"New Contact Form Submission from {name}",
                      recipients=['your_email@gmail.com'])
        msg.body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        # Send the email
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        print(f"Error sending email: {e}")
        flash('Failed to send message. Please try again later.', 'error')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)