from datetime import datetime
import requests
import selectorlib
import psycopg2 as pg


URL = "http://programmer100.pythonanywhere.com/"

connection = pg.connect("dbname=temp_scrape user=postgres password=4531")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS temperatures("
               "record_time timestamp,"
               "temperature real"
               ");")
connection.commit()
cursor.close()
connection.close()


def scrape(link):
    response = requests.get(link)
    text = response.text
    return text


def extract(text):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text)["temperature"]
    return value


def record(temperature):
    connection = pg.connect("dbname=temp_scrape user=postgres password=4531")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(%s, %s)", (datetime.now(), temperature))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    record(extracted)