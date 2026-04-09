from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# A simple backend API route
@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from your Python backend!"})

if __name__ == '__main__':
    # Render assigns the PORT environment variable automatically
    app.run(debug=True)