from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    temperature = random.randint(20, 35)
    humidity = random.randint(30, 70)
    return render_template("index.html", temp=temperature, hum=humidity)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
