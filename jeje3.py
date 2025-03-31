from flask import Flask, render_template, request
import os

app = Flask(__name__)

styles = [
    # Women styles
    {"id": 1, "name": "Elegant Braids", "price": 500, "image": "style1.jpg", "gender": "women"},
    {"id": 2, "name": "Twist Styles", "price": 400, "image": "style2.jpg", "gender": "women"},
    {"id": 3, "name": "Classic Cornrows", "price": 350, "image": "style3.jpg", "gender": "women"},

    # Men styles
    {"id": 4, "name": "Classic Fade", "price": 200, "image": "style4.jpg", "gender": "men"},
    {"id": 5, "name": "Taper Fade", "price": 250, "image": "style5.jpg", "gender": "men"},
    {"id": 6, "name": "Bold Afro", "price": 300, "image": "style6.jpg", "gender": "men"},
    {"id": 7, "name": "Undercut lång hair", "price": 400, "image": "style7.jpg", "gender": "men"},
    {"id": 8, "name": "Beard Trim", "price": 350, "image": "style8.jpg", "gender": "men"},
    {"id": 9, "name": "Taper Fade", "price": 220, "image": "style9.jpg", "gender": "men"}
]

@app.route('/')
def index():
    return render_template("home.html")

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
