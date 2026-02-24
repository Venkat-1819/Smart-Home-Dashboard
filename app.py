from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    temperature = random.randint(20, 35)
    humidity = random.randint(30, 70)
    return render_template("index.html", temp=temperature, hum=humidity)
