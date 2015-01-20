from flask import Flask

app = Flask(__disease__)
app.config.from_object('config')

from app import views
