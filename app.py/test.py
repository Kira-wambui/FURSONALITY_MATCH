from flask import Flask, render_template  # Import render_template

app = Flask(__name__)

@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')  # Make sure to render the HTML template