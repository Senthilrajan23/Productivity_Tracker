from datetime import datetime, UTC
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime, Null
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

#creating database
engine = create_engine('sqlite:///productivity.db', echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine)
db = session()

class WorkSession(Base):
    __tablename__ = 'Table'
    id = Column(Integer, primary_key=True)
    aux = Column(String, nullable=False)
    start_time = Column(DateTime, default=lambda: datetime.now()) #records time when the row is created
    end_time = Column(DateTime)

Base.metadata.create_all(engine)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/available', methods=['POST'])
def available():
    active_session = db.query(WorkSession).filter(WorkSession.end_time == None).first()

    # to throw an error if user clicks on the same aux again to avoid another row for same aux
    if active_session and active_session.aux == "Available":
        return render_template("base.html", error = " You are already in Available AUX!")

    if active_session:
        active_session.end_time = datetime.now()
    new_session = WorkSession(aux = "Available")
    db.add(new_session)
    db.commit()
    return render_template('base.html')  # productive_hours=productive_hours)

    """
    productive_hours = datetime.now().time().replace(microsecond=0).isoformat()
    
    hour = now.hour
    minute = now.minute
    productive_hours = round(((hour * 60 + minute)/60),2)
    """

@app.route("/learning", methods=['POST'])
def learning():

    #to find the active session i.e. the last formed row, where the end_time is Null
    active_session = db.query(WorkSession).filter(WorkSession.end_time == None).first()

    # to throw an error if user clicks on the same aux again to avoid another row for same aux
    if active_session and active_session.aux == "Learning":
        return render_template("base.html", error = " You are already in Learning AUX!")

    # To print the date and time, where the end_time is null
    if active_session:
        active_session.end_time = datetime.now(UTC)
    new_session = WorkSession(aux = "Learning")
    db.add(new_session)
    db.commit()
    return render_template('base.html')

@app.route("/break", methods=['POST'])
def learning():

    #to find the active session i.e. the last formed row, where the end_time is Null
    active_session = db.query(WorkSession).filter(WorkSession.end_time == None).first()

    # to throw an error if user clicks on the same aux again to avoid another row for same aux
    if active_session and active_session.aux == "break":
        return render_template("base.html", error = " You are already Break AUX!")

    # To print the date and time, where the end_time is null
    if active_session:
        active_session.end_time = datetime.now(UTC)
    new_session = WorkSession(aux = "Break")
    db.add(new_session)
    db.commit()
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug = True, port = 5002)