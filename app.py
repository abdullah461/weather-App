from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)



if __name__=='__main__':
    app.run(debug=True)