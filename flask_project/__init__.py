from flask import Flask

project = Flask(__name__)
project.config.from_object('config')

from . import views