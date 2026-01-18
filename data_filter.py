from bs4 import BeautifulSoup
import csv

print("Reading web_data.html")

# Read the HTML file
with open('../data/raw_data/web_data.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

print("Extracting market data...")

# Find market cards
market_data = []
market_cards = soup.find_all('div', class_='MarketCard-row')

for card in market_cards:
    try:
        # Find symbol 
        symbol_elem = card.find('span', class_='MarketCard-symbol')
        symbol = symbol_elem.text.strip() if symbol_elem else 'N/A'
        
        # Find stock position
        position_elem = card.find('span', class_='MarketCard-stockPosition')
        stock_position = position_elem.text.strip() if position_elem else 'N/A'
        
        # Find change percentage
        change_elem = card.find('span', class_='MarketCard-changePct')
        change_pct = change_elem.text.strip() if change_elem else 'N/A'
        
        market_data.append({
            'marketCard_symbol': symbol,
            'marketCard_stockPosition': stock_position,
            'marketCard-changePct': change_pct
        })
    except (AttributeError, TypeError) as e:
        continue

# Save market data to CSV
print("Storing market data to csv")
with open('../data/processed_data/market_data.csv', 'w', newline='', encoding='utf-8') as f:
    if market_data:
        writer = csv.DictWriter(f, 
            fieldnames=['marketCard_symbol', 'marketCard_stockPosition', 'marketCard-changePct'])
        writer.writeheader()
        writer.writerows(market_data)
        print("CSV created")

print("Extracting news data...")

# Find news items
news_data = []
news_items = soup.find_all('li', class_='LatestNews-item')

for item in news_items:
    try:
        # Find timestamp
        timestamp_elem = item.find('time', class_='LatestNews-timestamp')
        timestamp = timestamp_elem.text.strip() if timestamp_elem else 'N/A'
        
        # Find the link and title
        link_tag = item.find('a', class_='LatestNews-headline')
        
        if link_tag:
            title = link_tag.get('title', '').strip()
            link = link_tag.get('href', '').strip()
            
            news_data.append({
                'LatestNews-timestamp': timestamp,
                'title': title,
                'link': link
            })
    except (AttributeError, TypeError) as e:
        continue

# Save news data to CSV
print("Storing news data to csv")
with open('../data/processed_data/news_data.csv', 'w', newline='', encoding='utf-8') as f:
    if news_data:
        writer = csv.DictWriter(f, fieldnames=['LatestNews-timestamp', 'title', 'link'])
        writer.writeheader()
        writer.writerows(news_data)
        print("CSV created")

print("Filtering complete!")
print("CSV files created successfully.")