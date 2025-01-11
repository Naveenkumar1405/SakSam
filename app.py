from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, Response
from flask_mail import Mail, Message

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'saksamtechnologies@tenkasi627808'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'saksam.technologies2021@gmail.com'
app.config['MAIL_PASSWORD'] = 'zntw vdia djyv iugh'
app.config['MAIL_DEFAULT_SENDER'] = ('SakSam Technologies', 'saksam.technologies2021@gmail.com')

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

# Route for the gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route to handle form submission
@app.route('/send/contact', methods=['POST','GET'])
def send_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Name, Email, and Message are required fields.', 'error')
        return redirect(url_for('contact'))

    try:
        msg = Message(
            subject=f"New Contact Form Submission from {name}",
            recipients=['saksamtech21@gmail.com']
        )
        msg.body = f"""
        Hello SakSam Technologies Team,

        You have received a new message via the contact form on your website. Here are the details:

        -------------------------------------------
        👤 **Name**: {name}
        ✉️ **Email**: {email}
        📞 **Phone**: {phone if phone else "Not Provided"}
        -------------------------------------------

        📌 **Message**:
        {message}

        Thank you for using our contact form. We appreciate the opportunity to connect with you.

        Best Regards,
        Your SakSam Technologies Website
        """

        msg.html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                }}
                .container {{
                    width: 80%;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #555;
                }}
                .details {{
                    margin-top: 20px;
                    font-size: 16px;
                }}
                .footer {{
                    margin-top: 20px;
                    font-size: 14px;
                    color: #888;
                }}
                .highlight {{
                    color: #007BFF;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">📩 New Contact Form Submission</div>
                <hr>
                <div class="details">
                    <p><strong class="highlight">Name:</strong> {name}</p>
                    <p><strong class="highlight">Email:</strong> {email}</p>
                    <p><strong class="highlight">Phone:</strong> {phone if phone else "Not Provided"}</p>
                    <hr>
                    <p><strong class="highlight">Message:</strong></p>
                    <p>{message}</p>
                </div>
                <div class="footer">
                    <p>Best Regards,<br>SakSam Technologies Website</p>
                </div>
            </div>
        </body>
        </html>
        """
        # Sending the email
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return 'Success'
    except Exception as e:
        print(f"Error sending email: {e}")
        return 'Failed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)