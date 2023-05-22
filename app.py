import configparser
from flask import Flask, render_template, request

config = configparser.ConfigParser()
config.read('settings.ini')

app = Flask(__name__)


@app.route('/')
def index():

    return render_temp_fct()


@app.route('/start_action', methods=['POST'])
def start_action():
    return render_temp_fct()


def render_temp_fct():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
