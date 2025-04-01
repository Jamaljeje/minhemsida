from flask import Flask, render_template, request
import os

app = Flask(__name__)

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
    sorted_styles = sorted(filtered_styles, key=lambda s: s["price"])  # Sort by price
    return render_template("style.html", styles=sorted_styles)


@app.route('/book/<int:style_id>')
def book(style_id):
    selected_style = next((style for style in styles if style["id"] == style_id), None)
    return render_template("booking.html", style=selected_style)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
