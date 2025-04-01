from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
import smtplib

app = Flask(__name__)
app.secret_key = 'jejesecret123'

styles = [
    {"id": 1, "name": "Classic Fade", "price": 200, "image": "Classic_fade.jpg", "gender": "men"},
    {"id": 2, "name": "Beard Trim", "price": 250, "image": "Beard_trim.jpg", "gender": "men"},
    {"id": 3, "name": "Oil & Color", "price": 300, "image": "Collor_Oil.jpg", "gender": "men"},
    {"id": 4, "name": "Taper Fade", "price": 250, "image": "Taper_fade.jpg", "gender": "men"},
    {"id": 5, "name": "Undercut Long Hair", "price": 400, "image": "Undercut_long_Hair.jpg", "gender": "men"},
    {"id": 6, "name": "Beard Trim", "price": 350, "image": "Beard_trim.jpg", "gender": "men"},
    {"id": 7, "name": "Low Fade", "price": 220, "image": "Low_fade.jpg", "gender": "men"},
    {"id": 8, "name": "Bold Afro", "price": 300, "image": "Bold_Afro.jpg", "gender": "men"},
    {"id": 9, "name": "Twist Styles", "price": 400, "image": "twist_Styles.jpg", "gender": "women"},
    {"id": 10, "name": "Classic Cornrows", "price": 350, "image": "Classic_Cornrows.jpg", "gender": "women"},
    {"id": 11, "name": "Elegant Braids", "price": 500, "image": "Elegent_Braids.jpg", "gender": "women"},
]

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/styles')
def show_styles():
    gender = request.args.get('gender')
    filtered_styles = [style for style in styles if style["gender"] == gender] if gender else styles
    sorted_styles = sorted(filtered_styles, key=lambda s: s["price"])
    return render_template("style.html", styles=sorted_styles)

@app.route('/book/<int:style_id>', methods=['GET', 'POST'])
def book(style_id):
    selected_style = next((style for style in styles if style["id"] == style_id), None)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        datetime_str = request.form['datetime']
        selected_time = datetime.fromisoformat(datetime_str)

        # Calculate surcharge if booking time is < 30 mins away
        now = datetime.now()
        extra_charge = 30 if (selected_time - now).total_seconds() < 1800 else 0
        total_price = selected_style['price'] + extra_charge

        # Send booking email to you
        send_email(name, email, selected_style['name'], datetime_str, total_price)

        # Flash confirmation
        flash(f"Thanks {name}, your booking for {selected_style['name']} at {datetime_str} is confirmed! Total: {total_price} kr. We'll see you soon 💈")

        return redirect(url_for('book', style_id=style_id))

    return render_template("booking.html", style=selected_style)

def send_email(name, client_email, style_name, time, price):
    sender = "your_gmail@gmail.com"          # replace with your Gmail
    password = "your_app_password"           # use Gmail App Password!
    receiver = "jamaljeje22@gmail.com"       # your actual email

    subject = "New Booking from JejeKutz"
    body = f"""
    New booking received:

    Name: {name}
    Client Email: {client_email}
    Style: {style_name}
    Time: {time}
    Total Price: {price} kr
    """

    email_text = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email_text)
        print("Booking email sent ✅")
    except Exception as e:
        print("Error sending email:", e)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
