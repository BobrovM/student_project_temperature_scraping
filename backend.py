from datetime import datetime
import requests
import selectorlib


URL = "http://programmer100.pythonanywhere.com/"


def scrape(link):
    response = requests.get(link)
    text = response.text
    return text


def extract(text):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text)["temperature"]
    return value


def record(temperature):
    row = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    row += "," + str(temperature)+"\n"

    with open("data.txt", "a") as file:
        file.write(row)


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    record(extracted)