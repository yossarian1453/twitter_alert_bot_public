import psycopg2
import os

file_path = os.getcwd()

connection = psycopg2.connect("dbname=the_database_name user=the_user_you_use password=your_postgres_user_pass")
cursor = connection.cursor()
# cursor.execute("DROP TABLE IF EXISTS analysis.tweet_collection")
cursor.execute(f"""
    /*CREATE TABLE analysis.tweet_collection (
        date DATE,
        user_name VARCHAR,
        tweet VARCHAR
    );*/
    COPY analysis.tweet_collection
    FROM '{file_path}/stage_2/tweet_load.csv'
    WITH (FORMAT CSV, DELIMITER '|');
""")

connection.commit() # <--- makes sure the change is shown in the database 
connection.close()
cursor.close()
