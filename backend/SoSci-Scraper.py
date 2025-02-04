from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# service = Service(executable_path="chromedriver.exe")
driver = webdriver.Safari()

driver.get("https://www.socsc.hku.hk/sigc/credit-transfer-database/")

df = pd.DataFrame(columns=[
    'University',
    'University-Country',
    'Exchange-Course-Code',
    'Exchange-Course-Title',
    'HKU-Course-Code',
    'HKU-Course-Title'
])

uni_names = driver.find_elements(By.CLASS_NAME, "modal-title")[1:]
uni_number = 0

table_elements = driver.find_elements(By.CLASS_NAME, "uni")

for table_element in table_elements:
    print(uni_number)
    current_uni = uni_names[uni_number].text.split(" - ")[0]
    uni_country = uni_names[uni_number].text.split(" - ")[1]

    rows = table_element.find_elements(By.TAG_NAME, "tr")

    for row in rows[2:]:
        cells = row.find_elements(By.TAG_NAME, "td")

        new_row = {
            'University': current_uni,
            'University-Country': uni_country,
            'Exchange-Course-Code': cells[0].text,
            'Exchange-Course-Title': cells[1].text,
            'HKU-Course-Code': cells[3].text,
            'HKU-Course-Title': cells[4].text
        }

        # Append the new row to the DataFrame
        df.loc[len(df)] = new_row

    uni_number += 1

print(df)
driver.quit()

df.to_csv("sosci-credit_transfer_database.csv", index=False)
