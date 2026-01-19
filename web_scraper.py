from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# URL to scrape
url = "https://www.cnbc.com/world/?region=world"

print("Fetching data from CNBC using Selenium...")

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

# Create driver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # navigate to the URL 
    driver.get(url)
    
    # Wait for JavaScript to load content
    print("Waiting for dynamic content to load...")
    time.sleep(5)
    
    # Get the fully rendered page source
    html_content = driver.page_source
    print("Data fetched successfully!")
    
    # Save the raw HTML to file
    output_path = "../data/raw_data/web_data.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Data saved to {output_path}")
    
finally:
    driver.quit()
