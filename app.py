from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Routes for your HTML templates
@app.route('/')
def index():
    return render_template('Portfolio.html')

# Define other routes as needed for your sections (about, works, contact)

# Serve static files (CSS, images)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')