# Task 3
import pandas as pd
import logging
import psycopg2

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s --> %(funcName)s() --> %(message)s')
def insert_values():
    df = pd.read_csv('weather.csv')
    print(df.head())

    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')
        logging.info("Database successfully connected.")
        cur = connection.cursor()

        query = "Insert INTO weather (STATE, DESCRIPTION, TEMPERATURE, FEELS_LIKE_TEMPERATURE, MIN_TEMP, " \
            "MAX_TEMP, HUMIDITY,CLOUDS) values (%s,%s,%s,%s,%s,%s,%s,%s)"

        cur.execute("DELETE FROM weather;")

        for index, row in df.iterrows():
            cur.execute(query, (
                row['State'], row['Description'], row['Temperature'], row['Feels_Like_Temperature']
                , row['Min_Temperature'], row['Max_Temperature'], row['Humidity'], row['Clouds']))

        connection.commit()
        connection.close()
        logging.info("Values successfully inserted into table.")

    except Exception as e:
        logging.info("Error: ", e)

# insert_values()