--Создаем сперва зависимые таблицы, в которых хранятся профильные данные, чтоб появились параметры, на которые ссылаться основной таблице--
CREATE TABLE IF NOT EXISTS animal_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS animal_breed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS animal_color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS outcome_subtype (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS outcome_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);
--Теперь создаем основную таблицу, в которой прописываем связи с зависимыми таблицами. В базе может быть значение NULL--
-- в строках с именем и цветом, поэтому ограничение убираем --
CREATE TABLE IF NOT EXISTS new_animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age_upon_outcome VARCHAR (255) NOT NULL,
    animal_id VARCHAR (255) NOT NULL,
    name VARCHAR (255),
    date_of_birth TEXT,
    outcome_month INTEGER NOT NULL,
    outcome_year INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    breed_id INTEGER NOT NULL,
    color1_id INTEGER,
    color2_id INTEGER,
    outcome_subtype_id INTEGER,
    outcome_type_id INTEGER,

    FOREIGN KEY (type_id) REFERENCES animal_type(id),
    FOREIGN KEY (breed_id) REFERENCES animal_breed(id),
    FOREIGN KEY (color1_id) REFERENCES animal_color(id),
    FOREIGN KEY (color2_id) REFERENCES animal_type(id),
    FOREIGN KEY (outcome_subtype_id) REFERENCES animal_type(id),
    FOREIGN KEY (outcome_type_id) REFERENCES animal_type(id)
);