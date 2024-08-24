from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Web Application!"

@app.route('/add', methods=['GET'])
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return jsonify({"result": result})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a - b
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)