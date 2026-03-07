from datetime import datetime
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

#creating database
engine = create_engine('sqlite:///tasks.db', echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/clicked', methods=['POST'])
def clicked():
    productive_hours = datetime.now().time().replace(microsecond=0).isoformat()
    """
    hour = now.hour
    minute = now.minute
    productive_hours = round(((hour * 60 + minute)/60),2)
    """

    return render_template('base.html', productive_hours=productive_hours)

if __name__ == '__main__':
    app.run(debug = True, port = 5002)