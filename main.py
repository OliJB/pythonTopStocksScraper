from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

data = []

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
    #find individual columns in the rows and add to 'data' dictionary
    for row in rows:
        columns = row.find_elements(By.CLASS_NAME, "cell.tw-h-10.tw-py-0.yf-paf8n5")
        if len(columns) >= 11:
            data.append({
                "stock_symbol": columns[0].text,
                "stock_name": columns[1].text,
                "adv_chart" : columns [2].text,
                "stock_price": columns[3].text,
                "stock_change": columns[4].text,
                "stock_changePct": columns[5].text,
                "stock_volume": columns[6].text,
                "stock_avgVol": columns[7].text,
                "stock_mktCap": columns[8].text,
                "stock_peRatio": columns[9].text,
                "stock_52wkChangePct": columns[10].text,
                "52_week_rng" : columns[11].text
            })

#try except for error handling
except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()

#add dictionary to dataframe and remove unwanted columns
df = pd.DataFrame(data)
df = df.drop(columns=["adv_chart", "52_week_rng"])
print(df)

#set the file as a unique name & get downloads directory path
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"yahoo_top_gainers_{current_time}.csv"
downloads_path = str(Path.home() / "Downloads")
full_path = os.path.join(downloads_path, filename)

#save file to downloads foldery
print("Do you want a spreadsheet of the stocks? /n type Y or N")
user_input = input("Type y or n (Yes or No)")
if user_input == "y" or "Y":
    df.to_csv(full_path, index=False)
    print("File saved to downloads folder")
else:
    exit()
