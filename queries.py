GET_ANIMAL_BY_ID_SHORT_QUERY = """
    SELECT * FROM animals_new
    WHERE animal_id = :1;
"""

GET_ANIMAL_BY_ID_FULL_QUERY = """
    SELECT
        animals_new.id,
        age_upon_outcome,
        animal_id,
        animals_new.name,
        date_of_birth,
        outcom_month,
        outcom_year,
        animal_type.name as 'type',
        animal_breed.name as 'breed',
        animal_color1.name as 'color1',
        animal_color2.name as 'color2',
        outcome_subtype.name as 'outcome_subtype',
        outcome_type.name as 'outcome_type'    
    FROM animals_new
    LEFT JOIN animal_type
        ON animal_type.id = animals_new.animal_type_id
    LEFT JOIN animal_breed
        ON animal_breed.id = animals_new.breed_id
    LEFT JOIN animal_color as animal_color1
        ON animal_color1.id = animals_new.color1_id
    LEFT JOIN animal_color as animal_color2
        ON animal_color2.id = animals_new.color2_id
    LEFT JOIN outcome_subtype
        ON outcome_subtype.id = animals_new.outcome_subtype_id
    LEFT JOIN outcome_type
        ON outcome_type.id = animals_new.outcome_type_id
    WHERE animals_new.animal_id = :1
"""