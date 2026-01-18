import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"

# add headers to mimic a real browser 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("Fetching data from CNBC...")

response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully!")
    
    output_path = "../data/raw_data/web_data.html"
    
    # save scraped data to output path 
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f"Data saved to {output_path}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")