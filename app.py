from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eric')
def eric():
    return render_template('eric.html')

if __name__ == '__main__':
    app.run(debug=True)