from flask import Flask, render_template
from config import conf

app = Flask(__name__)

@app.route('/')
def countdown():
    input_msg = conf.get('msg', '')
    input_date = conf.get('date', '')
    return render_template('countdown.html', msg = input_msg, date = input_date)
