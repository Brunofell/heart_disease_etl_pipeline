from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3307/heart_disease")
create_table_sql = """
    CREATE TABLE IF NOT EXISTS heart_disease(
        age INTEGER,
        sex INTEGER,
        chest_pain_type INTEGER,
        bp INTEGER,
        cholesterol INTEGER,
        fbs_over_120 INTEGER,
        ekg_results INTEGER,
        max_hr INTEGER,
        exercise_angina INTEGER,
        st_depression FLOAT,
        slope_of_st INTEGER,
        number_of_vessels_fluro INTEGER,
        thallium INTEGER,
        heart_disease VARCHAR(30)
    );
"""

with engine.connect() as con:
    con.execute(text(create_table_sql))
    print("OK!!!!!")
