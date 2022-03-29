import sqlite3
from os.path import isfile, join

from settings import DATABASE_PATH, SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH, DATA_MIGRATION_FILE_PATH


def get_sql_from_file(file_name):
    """
    Получает sql из файла
    :param file_name: Путь до файла
    :return: Запрос
    """
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
    return content


def main():
    """
    Основная функция, выполняет миграцию данных.
    :return:
    """
    with sqlite3.connect(DATABASE_PATH) as con:
        cur = con.cursor()

        # Создаем структуру базы
        init_sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
        cur.executescript(init_sql)

        # Заполняем данными
        data_sql = get_sql_from_file(join(SQL_DIR_PATH, DATA_MIGRATION_FILE_PATH))
        cur.executescript(data_sql)


if __name__ == '__main__':
    main()
