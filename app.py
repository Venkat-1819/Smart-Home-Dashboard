from flask import Flask, render_template, redirect, url_for
import random
temp_history = []

app = Flask(__name__)

# Device states
light_status = "OFF"
fan_status = "OFF"

temp_history = []

@app.route('/')
def index():
    global temp_history

    temp = random.randint(20, 35)

    temp_history.append(temp)

    if len(temp_history) > 10:
        temp_history.pop(0)

    return render_template("index.html",
                           temp=temp,
                           light=light_status,
                           fan=fan_status,
                           temps=temp_history)


@app.route('/light_on')
def light_on():
    global light_status
    light_status = "ON"
    return redirect(url_for('home'))

@app.route('/light_off')
def light_off():
    global light_status
    light_status = "OFF"
    return redirect(url_for('home'))

@app.route('/fan_on')
def fan_on():
    global fan_status
    fan_status = "ON"
    return redirect(url_for('home'))

@app.route('/fan_off')
def fan_off():
    global fan_status
    fan_status = "OFF"
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)