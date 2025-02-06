from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Setup Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Start the WebDriver
driver = webdriver.Chrome(options=options)

# URL to scrape
url = "https://www.wsj.com/market-data/stocks/us/movers"
driver.get(url)

# Give the page time to load JavaScript-rendered content
time.sleep(5)

# Extract table data
tables = pd.read_html(driver.page_source)

# Save the first table to CSV (adjust index if needed)
if tables:
    tables[0].to_csv("sample_data/wjsgainers.csv", index=False)
    print("WSJ gainers saved to sample_data/wjsgainers.csv")
else:
    print("No tables found on WSJ page.")

# Close the driver
driver.quit()
