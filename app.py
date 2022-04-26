from flask import flask_template
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float (form['radius'])
        height = float (form['height'])
        estimate=radius+height
        return render_template('estimate.html', data=estimate)
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)