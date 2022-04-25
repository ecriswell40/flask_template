from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    if request.method == 'POST'
    form = request.form
    height = form['height']
    radius = form['radius']
    return redirect(url_for('estimate'))
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)