from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from random import choice
from string import digits
import datetime

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
    result = cursor.execute("SELECT ID, name, currentStatus, team, year, rushingYards, rushingTDs, fumbles "
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
    result = cursor.execute("SELECT ID, name, currentStatus, DOB "
                            "FROM Player "
                            "LIMIT 2000;")
    data = cursor.fetchall()
    rows = []
    cols = []

    for row in data:
        for col in row:
            cols.append(col)
        rows.append(cols)
        cols = []
    # for row in rows:
    #     row[3] = datetime.datetime.strftime(row[3], '%m, %d, %Y')
    return render_template('delete.html', activePage=activePage, data=rows)


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
        team = request.form['team']
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
            msg = {'Player was not successfully added to database. The following exception occurred': [str(e)]}
            print(msg)
            flash(msg,
                  'error')
            return redirect(url_for('index'))
    print(form.errors)
    flash(form.errors, 'error')
    return redirect(url_for('index'))


@app.route('/update_player', methods=['GET', 'POST'])
def update_player():
    form = request.form
    if form:
        id = form['id']
        team = form['team']
        year = form['year']
        fumbles = form['fumbles']
        rushingYards = form['rushingYards']
        rushingTDs = form['rushingTDs']

        try:
            result = cursor.execute("UPDATE Rushing SET rushingYards = {}, rushingTDs = {}, fumbles = {} "
                                    "WHERE (playerID LIKE \"{}\" AND team LIKE \"{}\" AND year = {})"
                                    .format(rushingYards, rushingTDs, fumbles, id, team, year))
            conn.commit()
            flash('Player was successfully updated. {} row affected.'.format(result), 'success')
            return redirect(url_for('update'))
        except Exception as e:
            msg = {'Player was not successfully updated. The following exception occurred': [str(e)]}
            print(msg)
            flash(msg,
                  'error')
            return redirect(url_for('update'))
    print(form.errors)
    flash(form.errors, 'error')
    return redirect(url_for('update'))


@app.route('/delete_player', methods=['GET', 'POST'])
def delete_player():
    try:
        form = request.form
        id = form['id']
        cursor.execute("DELETE FROM Rushing WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM Passing WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM Receiving WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM FieldGoalKicking WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM Defensive WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM Stats WHERE playerID LIKE \"{}\"".format(id))
        cursor.execute("DELETE FROM Player WHERE ID LIKE \"{}\"".format(id))
        conn.commit()
        flash('Player was successfully deleted. 7 tables affected.', 'success')
        return redirect(url_for('delete'))
    except Exception as e:
        msg = {'Player was not successfully deleted. The following exception occurred': [str(e)]}
        print(msg)
        flash(msg,
              'error')
        return redirect(url_for('delete'))


class PlayerForm(Form):
    name = StringField('name', [validators.Length(min=1, max=50), validators.DataRequired()])
    day = IntegerField('day', [validators.DataRequired()])
    month = IntegerField('month', [validators.DataRequired()])
    year = IntegerField('year', [validators.DataRequired()])


if __name__ == '__main__':
    app.run()
