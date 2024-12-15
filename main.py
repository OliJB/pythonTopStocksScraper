from selenium import webdriver
from selenium.webdriver.common.by import By

#define url and webdriver
url = 'https://finance.yahoo.com/markets/stocks/gainers/'
driver = webdriver.Firefox()

#start the scrape, opening the website & ensure time for loading
driver.get(url)
driver.implicitly_wait(10)

#get past the cookies acceptance
driver.find_element(By.ID,'scroll-down-btn').click()
accept_button = driver.find_element(By.CLASS_NAME, 'btn.secondary.accept-all')
accept_button.click()

try:
    # Find all rows with the specific class name
    rows = driver.find_elements(By.CLASS_NAME, "row.false.yf-paf8n5")

    # Loop through each row and print the scraped data
    for index, row in enumerate(rows):
        print(f"Row {index + 1}:")
        print(row.text)
        print("-" * 50)

#try except for error handling
except Exception as e:
    print(f"An error occurred: {e}")
