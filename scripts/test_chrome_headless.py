from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

with webdriver.Chrome(options=options) as driver:
    driver.get("https://example.com")
    page_source = driver.page_source

    with open("sample_data/ygainers.csv", "w", encoding="utf-8") as file:
        file.write(page_source)

    print("Page source saved to sample_data/ygainers.csv")
