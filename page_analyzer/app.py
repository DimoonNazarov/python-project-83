

from flask import Flask, render_template, get_flashed_messages
from dotenv import load_dotenv
import os
from page_analyzer.db import (get_all_urls, get_urls_by_id, get_checks_by_id)

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/urls")
def urls():
    urls = get_all_urls()
    return render_template('urls.html', urls=urls)


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.route("/urls/<int:id_>")
def url_show(id_):
    try:
        url  = get_urls_by_id(id_)
        checks = get_checks_by_id(id_)
        messages = get_flashed_messages(with_categories=True)
        return render_template(
            'show.html',
                               url=url,
                               checks =checks,
                               messages= messages
        )
    except IndexError:
        return render_template("404.html"), 404