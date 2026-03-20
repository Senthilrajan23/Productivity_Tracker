from datetime import datetime
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime, Null, func
from sqlalchemy.orm import sessionmaker, relationship, Session, declarative_base
#from sqlalchemy.ext.declarative
from sqlalchemy.exc import IntegrityError

#creating database
engine = create_engine('sqlite:///productivity.db', echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine)
db = session()

#Table creation
class WorkSession(Base):
    __tablename__ = 'Table'
    id = Column(Integer, primary_key=True)
    aux = Column(String, nullable=False)
    start_time = Column(DateTime, default=lambda: datetime.now()) #records time when the row is created
    end_time = Column(DateTime)

Base.metadata.create_all(engine)

app = Flask(__name__)


# Utility function to avoid repeated lines of code
def switch_aux(aux_name):
    active_session = db.query(WorkSession).filter(WorkSession.end_time == None).first()

    if active_session and active_session.aux == aux_name:
        return render_template("base.html", error=f"You are already in {aux_name} AUX!")

    if active_session:
        active_session.end_time = datetime.now()

    new_session = WorkSession(aux = aux_name)
    db.add(new_session)
    db.commit()
    return render_template("base.html")



@app.route('/')
def index():
    return render_template("base.html")

@app.route('/available', methods=['POST'])
def available():
    return switch_aux("Available")

@app.route("/learning", methods=['POST'])
def learning():
    return switch_aux("Learning")
""" 

    
    active_session = db.query(WorkSession).filter(WorkSession.end_time == None).first()

    
    if active_session and active_session.aux == "Learning":
        return render_template("base.html", error = " You are already in Learning AUX!")

    
    if active_session:
        active_session.end_time = datetime.now(UTC)
    new_session = WorkSession(aux = "Learning")
    db.add(new_session)
    db.commit()
    return render_template('base.html')
    """

@app.route("/break", methods=['POST'])
def break_aux():
    return switch_aux("Break")
"""
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
"""

@app.route("/coding", methods = ["POST"])
def coding():
    return switch_aux("Coding")

@app.route("/entertainment", methods = ["POST"])
def entertainment():
    return switch_aux("Entertainment")

@app.route("/offline", methods=['POST'])
def offline():
    return switch_aux("Offline")
"""
@app.route('/result', methods=['POST'])
def result():
    
    result = db.query(WorkSession.aux), func.sum(func.strftime('%s', func.coalesce(WorkSession.end_time, func.current_timestamp())) - func.strftime('%s', WorkSession.start_time)).label("total_seconds")).group_by(WorkSession.aux).all()
    return render_template("base.html",result=result)
"""

today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
@app.route('/result', methods=['POST'])
def result():
    result = db.query(
        WorkSession.aux,
        func.sum(
            func.strftime('%s', func.coalesce(WorkSession.end_time, func.localtimestamp())) -
            func.strftime('%s', WorkSession.start_time)
        ).label("total_seconds")
    ).filter(
        WorkSession.start_time >= today_start
    ).group_by(WorkSession.aux).all()


    # Formatting time from seconds to minutes
    def format_time(seconds):
        if seconds < 60:
            return f"{seconds} seconds"

        minutes = seconds // 60
        if minutes < 60:
            return f"{minutes} minutes"

        hours = minutes // 60

        remaining_time = minutes % 60
        return f"{hours} hr {remaining_time} minutes"

    format_result = []
    for aux, total_seconds in result:
        formatted_time = format_time(total_seconds)
        format_result.append((aux, formatted_time))

    return render_template("base.html", result=format_result)


#@app.route("")
if __name__ == '__main__':
    app.run(debug = True, port = 5002)