from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Updated styles with correct image filenames from static/
styles = [
    # Men styles
    {"id": 1, "name": "Classic Fade", "price": 200, "image": "style1.jpg", "gender": "men"},
    {"id": 2, "name": "Beard Trim", "price": 250, "image": "style2.jpg", "gender": "men"},
    {"id": 3, "name": "Oil & Color", "price": 300, "image": "style3.jpg", "gender": "men"},

    # Women styles
    {"id": 4, "name": "Elegant Braids", "price": 500, "image": "style4.jpg", "gender": "women"},
    {"id": 5, "name": "Twist Styles", "price": 400, "image": "style5.jpg", "gender": "women"},
    {"id": 6, "name": "Classic Cornrows", "price": 350, "image": "style6.jpg", "gender": "women"},

    # Extra styles
    {"id": 7, "name": "Side Shave", "price": 280, "image": "style7.jpg", "gender": "men"},
    {"id": 8, "name": "Bold Afro", "price": 450, "image": "style8.jpg", "gender": "women"},
    {"id": 9, "name": "Taper Fade", "price": 220, "image": "style9.jpg", "gender": "men"},
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/styles')
def show_styles():
    gender = request.args.get('gender')
    filtered_styles = [style for style in styles if style["gender"] == gender] if gender else styles
    return render_template("style.html", styles=filtered_styles)

@app.route('/book/<int:style_id>')
def book(style_id):
    selected_style = next((style for style in styles if style["id"] == style_id), None)
    return render_template("booking.html", style=selected_style)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
