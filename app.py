import sqlite3

from flask import Flask, jsonify

import queries
from settings import DATABASE_PATH

app = Flask(__name__)


def serialize_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/<animal_id>')
def get_animal_by_id_short(animal_id):
    """Возвращает информацию об объекте по его id, в короткой форме"""

    connection: sqlite3.Connection = app.config['db']
    cursor = connection.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_SHORT_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


@app.route('/<animal_id>/full')
def get_animal_by_id_full(animal_id):
    """Возвращает информацию об объекте по его id, в полной форме"""

    connection: sqlite3.Connection = app.config['db']
    cursor = connection.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_FULL_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


if __name__ == '__main__':
    con = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    app.config['db'] = con
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        con.close()
