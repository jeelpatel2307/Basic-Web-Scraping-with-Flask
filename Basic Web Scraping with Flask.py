from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_quotes():
    """
    Scrape quotes from http://quotes.toscrape.com and return a list of dictionaries.
    Each dictionary contains the quote text and author.
    """
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = []
        
        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            quotes.append({"text": text, "author": author})
        
        return quotes
    else:
        return []

@app.route("/")
def home():
    quotes = get_quotes()
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quotes Web Scraping</title>
</head>
<body>
    <h1>Quotes Web Scraping</h1>
    <ul>
        {% for quote in quotes %}
            <li>"{{ quote.text }}" - {{ quote.author }}</li>
        {% endfor %}
    </ul>
</body>
</html>
