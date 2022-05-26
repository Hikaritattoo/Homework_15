import sqlite3
from os.path import join, isfile

DATABASE_PATH = 'animal.db'
SQL_DIR_PATH = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'
DATA_MIGRATION_FILE_PATH = 'migrate.sql'


def get_sql_from_file(file_name):
    """получает чистый sql из базы"""
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
    return content


def main():
    """Функция, которая выполняет миграцию данных"""

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH, DATA_MIGRATION_FILE_PATH))

    cursor.executescript(sql)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
