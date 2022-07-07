from urllib import response
from flask import Flask, render_template, request,  jsonify

import re
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template('base.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    text = re.sub(r'[^a-zA-Z]', '', text)

    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True) #Debug=True for testing purposes