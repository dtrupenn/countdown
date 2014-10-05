from flask import Flask, render_template, request, send_from_directory

from config import conf

app = Flask(__name__)

@app.route('/imgs/line.jpg', methods=['GET'])
@app.route('/imgs/bkgdimage.gif', methods=['GET'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def countdown():
    input_msg = conf.get('msg', '')
    input_date = conf.get('date', '')
    return render_template('countdown.html', msg = input_msg, date = input_date)
