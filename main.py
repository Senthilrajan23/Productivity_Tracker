from datetime import datetime, UTC
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

#creating database
engine = create_engine('sqlite:///productivity.db', echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    aux = Column(String, nullable=False)
    start_time = Column(DateTime, default=lambda: datetime.now(UTC)) #records time when the row is created
    end_time = Column(DateTime)

Base.metadata.create_all(engine)
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