from flask import Flask, render_template, request, redirect, url_for
import pickle
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Login credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('home'))
    else:
        return "Invalid Username or Password"

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    water = int(request.form['water'])
    junk_food = int(request.form['junk_food'])
    fruits = int(request.form['fruits'])
    meals = int(request.form['meals'])
    sleep = int(request.form['sleep'])
    exercise = int(request.form['exercise'])

    features = [[water, junk_food, fruits, meals, sleep, exercise]]

    prediction = model.predict(features)

    return render_template(
        'index.html',
        prediction_text=f"Your Food Habit is: {prediction[0]}"
    )

@app.route('/chart')
def chart():

    data = pd.read_csv('food_dataset.csv')

    counts = data['result'].value_counts()

    plt.figure(figsize=(5,5))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
    plt.title('Food Habit Distribution')

    plt.savefig('static/chart.png')
    plt.close()

    return render_template('chart.html')

if __name__ == '__main__':
    app.run(debug=True)