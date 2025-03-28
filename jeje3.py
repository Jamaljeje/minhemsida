from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Styles and Prices
styles = {
    'men': [
        {'name': 'Classic Fade', 'price': 200},
        {'name': 'Beard Trim', 'price': 250},
        {'name': 'Oil & Color', 'price': 300},
    ],
    'women': [
        {'name': 'Elegant Braids', 'price': 500},
        {'name': 'Twist Styles', 'price': 400},
        {'name': 'Classic Cornrows', 'price': 350},
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/styles')
def styles_page():
    gender = request.args.get('gender')
    selected_styles = styles.get(gender, [])
    return render_template('style.html', styles=selected_styles, gender=gender)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    style_name = request.args.get('style')
    gender = request.args.get('gender')

    # Find the selected style's price
    selected_style = None
    for style in styles.get(gender, []):
        if style['name'] == style_name:
            selected_style = style
            break

    if not selected_style:
        return "Style not found", 404

    final_price = selected_style['price']
    adjustment_note = ""

    if request.method == 'POST':
        selected_datetime = request.form.get('datetime')
        if selected_datetime:
            booking_time = datetime.fromisoformat(selected_datetime)
            now = datetime.now()
            delta = booking_time - now

            if delta < timedelta(minutes=30):
                final_price += 30
                adjustment_note = "⚠️ +30 kr for short notice booking (less than 30 mins)"
            elif delta >= timedelta(days=2):
                final_price -= 20
                adjustment_note = "🎉 -20 kr discount for booking 2 days ahead!"

    return render_template(
        'booking.html',
        style=style_name,
        price=selected_style['price'],
        final_price=final_price,
        adjustment_note=adjustment_note,
        gender=gender
    )

if __name__ == '__main__':
    app.run(debug=True, port=8080)
