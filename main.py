from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    return jsonify({"message": "Flask server is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)