from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/urls")
def urls():
    return render_template('urls.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404