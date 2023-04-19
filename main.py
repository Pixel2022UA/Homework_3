import sqlite3
import os

import flask

import create_db


app = flask.Flask(__name__)


@app.route("/")
def main():
    return "This is index page"


@app.route("/names")
def names():
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute("SELECT first_name FROM customers")
    rows = cur.fetchall()
    count_names = len(rows)
    my_set = {row[0] for row in rows}
    count_set = len(my_set)
    return flask.render_template("names.html", count_set=count_set, count_names=count_names)


@app.route("/tracks")
def tracks():
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute("SELECT title FROM tracks")
    rows = cur.fetchall()
    count_tracks = len(rows)
    return flask.render_template("count_tracks.html", count_tracks=count_tracks)


@app.route("/tracks-sec")
def tracks_sec():
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM tracks")
    rows = cur.fetchall()
    return flask.render_template("tracks-sec.html", rows=rows)


def main():
    if not os.path.exists('mydatabase.db'):
        create_db.create_db()
    app.run(debug=True)


if __name__ == "__main__":
    main()
