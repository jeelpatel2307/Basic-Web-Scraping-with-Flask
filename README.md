# Basic Web Scraping with Flask

This project is a basic demonstration of web scraping using Flask, where quotes are scraped from [http://quotes.toscrape.com](http://quotes.toscrape.com/) and displayed on a web page.

## How It Works

1. **Web Scraping Function:**
    - The `get_quotes` function in `app.py` performs web scraping on [http://quotes.toscrape.com](http://quotes.toscrape.com/) using BeautifulSoup.
    - It extracts quote text and author information and returns a list of dictionaries.
2. **Flask Route:**
    - The `/` route in the Flask app calls the `get_quotes` function to obtain quotes.
    - The obtained quotes are rendered on the `index.html` template.
3. **HTML Template:**
    - The HTML template (`index.html`) displays the quotes in a simple list format.

## Usage

1. **Run the Flask App:**
    - Save the script in a file, for example, `app.py`.
    - Install Flask and BeautifulSoup using the following commands:
        
        ```bash
        pip install Flask
        pip install beautifulsoup4
        
        ```
        
    - Run the script using a Python interpreter:
        
        ```bash
        python app.py
        
        ```
        
    - Open a web browser and go to http://127.0.0.1:5000/ to view the quotes obtained from web scraping.
2. **Customization:**
    - Modify the web scraping logic in the `get_quotes` function for different websites or data.
    - Enhance the HTML template (`index.html`) to include additional styling or features.

Feel free to explore and modify this project based on your interests and requirements!

---

## Author

Jeel patel
