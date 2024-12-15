from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.monster.co.uk/jobs/search?q=software+engineer&where=London%2C+England&page=1&so=m.h.lh'
url_2 = 'https://www.python.org/'
url_3 = 'https://finance.yahoo.com/markets/stocks/gainers/'
driver = webdriver.Firefox()

driver.get(url_3)

driver.implicitly_wait(10)

driver.find_element(By.ID,'scroll-down-btn').click()
accept_button = driver.find_element(By.CLASS_NAME, 'btn.secondary.accept-all')
accept_button.click()


try:
    # Find all rows with the specific class name
    rows = driver.find_elements(By.CLASS_NAME, "row.false.yf-paf8n5")

    # Loop through each row and print its text
    for index, row in enumerate(rows):
        print(f"Row {index + 1}:")
        print(row.text)  # Extract and print all text content in the row
        print("-" * 50)  # Separator for better readability

except Exception as e:
    print(f"An error occurred: {e}")
