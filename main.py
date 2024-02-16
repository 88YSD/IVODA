from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
import phonenumbers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwert321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voda.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
