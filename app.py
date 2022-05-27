from flask import Flask, jsonify
import sqlite3
import query

app = Flask(__name__)
DATABASE_PATH = 'animal.db'


def serialize_rows(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/<animal_id>')
def search_by_animal(animal_id):
    connection: sqlite3.Connection = app.config['db']
    cursor = connection.cursor()
    cursor.execute(query.GET_ANIMAL_DATA_BY_ID, (animal_id,))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_rows(row))


if __name__ == '__main__':
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config['db'] = connection
    try:
        app.run()
    except KeyboardInterrupt:
        connection.close()

# connection: sqlite3.Connection = app.config['db'] - информация,
# которая не влияет на код, а помогает понять IDE, с каким форматом мы работаем

# так же передаем в параметры запроса cursor.execute кортеж с первым значением в виде (animal_id,)

# для сериализации json прописываем connection.row_factory = sqlite3.Row
# и создаем функцию, которая поможет sqlite вывести нужные данные

# чтоб выводить json из flask, используем jsonfy
