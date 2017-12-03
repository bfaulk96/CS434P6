from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from random import choice
from string import digits

from wtforms import Form, StringField, IntegerField, validators

app = Flask(__name__)

app.secret_key = 'my unobvious secret key'

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Password1!'
app.config['MYSQL_DATABASE_DB'] = 'project6'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def index():
    activePage = 'index'
    return render_template('index.html', activePage=activePage)


@app.route('/update')
def update():
    activePage = 'update'
    result = cursor.execute("SELECT ID, name, currentStatus, year, rushingYards, rushingTDs, fumbles "
                            "FROM Player, Rushing "
                            "WHERE ID = playerID "
                            "LIMIT 2000;")
    data = cursor.fetchall()
    rows = []
    cols = []

    for row in data:
        for col in row:
            cols.append(col)
        rows.append(cols)
        cols = []

    return render_template('update.html', activePage=activePage, data=rows)


@app.route('/delete')
def delete():
    activePage = 'delete'
    return render_template('delete.html', activePage=activePage)


@app.route('/interesting')
def interesting():
    activePage = 'interesting'
    return render_template('interesting.html', activePage=activePage)


@app.route('/insert_player', methods=['GET', 'POST'])
def insert_player():
    form = PlayerForm(request.form)
    if form.validate():
        name = request.form['name']
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']
        status = request.form['status']
        dob = year + '-' + month + '-' + day
        playerID = name.strip(" ").lower() + '/' + (''.join(choice(digits) for i in range(7)))

        try:
            result = cursor.execute(
                "INSERT INTO Player(name, DOB, currentStatus, ID) "
                "VALUES ('{}','{}','{}','{}')".format(name, dob, status, playerID))
            conn.commit()
            flash('Player was successfully added to the database. {} row affected.'.format(result), 'success')
            return redirect(url_for('index'))
        except Exception as e:
            msg = {'Player was not successfully added to database. The following exception occured': [str(e)]}
            print(msg)
            flash(msg,
                  'error')
            return redirect(url_for('index'))
    print(form.errors)
    flash(form.errors, 'error')
    return redirect(url_for('index'))


class PlayerForm(Form):
    name = StringField('name', [validators.Length(min=1, max=50), validators.DataRequired()])
    day = IntegerField('day', [validators.DataRequired()])
    month = IntegerField('month', [validators.DataRequired()])
    year = IntegerField('year', [validators.DataRequired()])


if __name__ == '__main__':
    app.run()
