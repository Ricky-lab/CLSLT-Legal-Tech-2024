from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

lawyers_data = [
    # Dummy data, add more mock lawyers as needed
    {"id": 1, "name": "John Doe", "languages": ["English"], "price": 200, "experience": 5, "rating": 4.5},
    {"id": 2, "name": "Jane Smith", "languages": ["English", "Spanish"], "price": 250, "experience": 8, "rating": 4.7},
]

@app.route('/get-lawyers', methods=['POST'])
def get_lawyers():
    # Would process the request data to filter lawyers
    return jsonify(lawyers_data)


# The matching algorithm
def match_lawyers(preferred_language=None, max_price=None):
    matched_lawyers = [lawyer for lawyer in lawyers_data if (preferred_language in lawyer["languages"] or preferred_language is None) and (lawyer["price"] <= max_price or max_price is None)]
    return matched_lawyers

# Frontend implementation.
@app.route('/')
def index():
    return app.send_static_file('index.html')  # Assuming you have an 'index.html' in your 'static' folder

