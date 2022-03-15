# Task 2
import psycopg2
import logging
logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s --> %(funcName)s() --> %(message)s')

def insert_column_header():
    query = """CREATE TABLE weather(
            STATE VARCHAR(30),
            DESCRIPTION varchar(30),
            TEMPERATURE decimal,
            FEELS_LIKE_TEMPERATURE decimal,
            MIN_TEMP decimal,
            MAX_TEMP decimal,
            HUMIDITY numeric,
            CLOUDS numeric)"""
    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')
        logging.info("Database successfully connected.")
        cur = connection.cursor()
        logging.info("Cursor defined")
        cur.execute(query)
        connection.commit()
        connection.close()
        logging.info("Successfully created table.")

    except Exception as e:
        logging.info("Error: ", e)


# insert_column_header()
