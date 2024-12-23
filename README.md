# Hillswear Web Scraper

This is a web scraper built using Python and Selenium for automating the process of searching and extracting product details from the **Hillswear** website (https://hillswear.com/pl). The scraper is designed to search for a specific product and retrieve its price.

## Features:
- **Automatic Search**: The scraper can automatically search for products by their names, e.g., "T Shirt".
- **Price Extraction**: It retrieves the regular price of the product, including its currency.
- **Cookie Handling**: The script accepts cookies upon visiting the website to ensure seamless scraping.
- **Browser Automation**: Uses Selenium WebDriver to interact with the website, mimicking human behavior (clicking buttons, scrolling, etc.).

## Technologies Used:
- **Python 3.9.6**
- **Selenium**: For web automation and scraping.
- **ChromeDriver**: Browser automation with the Google Chrome browser.
- **webdriver-manager**: For managing the ChromeDriver version.

## How to Use:
1. Clone this repository:
   ```
   git clone https://github.com/Rainbowmindd/HillsBot
   ```
2. Install the required dependencies:
   ```
   pip install selenium
   pip install webdriver-manager
   ```
2. Run the script:
   ```
   python3 main.py
   ```

## Functionality:
- The script first accepts cookies on the website if prompted.
- Then, it searches for a product by name (e.g., "T Shirt").
- After the product page loads, it extracts the price of the product.
- The price is printed to the console, showing the regular price of the selected product.

## Future Improvements:
- Add functionality to check if the product is on sale and return the sale price if applicable.
- Handle more edge cases for dynamic web content and errors.
