from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Define the Contact Form using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField('Email', validators=[DataRequired(message="Please enter your email."), Email(message="Invalid email address.")])
    message = TextAreaField('Message', validators=[DataRequired(message="Please enter your message.")])
    submit = SubmitField('Submit')

# Route for the Home/Dashboard Page
@app.route('/')
def home():
    return render_template('index.html', form=ContactForm())

# API Route to Serve Raw Data
@app.route('/api/raw-data')
def raw_data():
    try:
        data = pd.read_csv(os.path.join('assets', 'data', 'raw.csv'))
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Route for Uninsured Young Data
@app.route('/api/uninsuredyoung-data')
def uninsuredyoung_data():
    try:
        data = pd.read_csv(os.path.join('assets', 'data', 'uninsuredyoung.csv'))
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Route for Benchmark Premiums Data
@app.route('/api/benchmarkprems-data')
def benchmarkprems_data():
    try:
        data = pd.read_csv(os.path.join('assets', 'data', 'benchmarkprems.csv'))
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to Handle Contact Form Submission
@app.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Extract form data
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # TODO: Implement email sending functionality here
        # For example, using Flask-Mail or an external email service

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('home'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
