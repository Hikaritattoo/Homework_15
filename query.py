GET_ANIMAL_DATA_BY_ID = """
        SELECT 
            new_animals.id,
            animal_id,
            age_upon_outcome,
            new_animals.name,
            date_of_birth,
            outcome_month,
            outcome_year,
            animal_type.name as 'type_id',
            animal_breed.name as 'breed_id',
            animal_color1.name as 'color1',
            animal_color2.name as 'color2',
            outcome_subtype.name as 'outcome_subtype',
            outcome_type.name as 'outcome_type'
        FROM new_animals
        LEFT JOIN animal_type
            ON animal_type.id = new_animals.type_id
        LEFT JOIN animal_breed
            ON animal_breed.id = new_animals.breed_id
        LEFT JOIN animal_color as animal_color1
            ON animal_color1.id = new_animals.color1_id
        LEFT JOIN animal_color as animal_color2
            ON animal_color2.id = new_animals.color2_id
        LEFT JOIN outcome_subtype
            ON outcome_subtype.id = new_animals.outcome_subtype_id
        LEFT JOIN outcome_type
            ON outcome_type.id = new_animals.outcome_type_id
        WHERE new_animals.animal_id = :1
"""

# отдельный файл для запроса данных из новой таблицы new_animals
