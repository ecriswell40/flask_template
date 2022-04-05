from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def /():
    return render_template('base.html')

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)