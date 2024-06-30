import pandas as pd
import csv
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from wtforms import form
from morse_converter import Morse
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

morse = Morse()


@app.route('/', methods=['get', 'post'])
def home():
    to_convert = "Type some text into the box and convert it to Morse Code!"
    if request.method == 'POST':
        to_convert = request.form['to_convert']
        converted_string = morse.convert_string(to_convert)
        return render_template('home.html', converted_string=converted_string, to_convert=to_convert)
    return render_template('home.html', to_convert=to_convert)


if __name__ == "__main__":
    app.run(debug=True)

