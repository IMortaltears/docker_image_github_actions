from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.entry import Entry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time_tracker.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    activity = request.form['activity']
    start_time = request.form['start_time']
    end_time = request.form['end_time']

    entry = Entry(activity=activity, start_time=start_time, end_time=end_time)
    db.session.add(entry)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
