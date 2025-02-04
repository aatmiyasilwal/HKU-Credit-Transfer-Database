from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# service = Service(executable_path="chromedriver.exe")
driver = webdriver.Safari()
url = "https://www.fbeitt.hku.hk/exchange-ctdb/index.php?fuseaction=site.course&partner_id="
uni_id = 1

df = pd.DataFrame(columns=[
    'University',
    'University-Country',
    'Exchange-Course-Code',
    'Exchange-Course-Title',
    'HKU-Course-Code',
    'HKU-Course-Title'
])


for uni_id in range(1, 307):
    driver.get(f"{url}{str(uni_id)}")

    uni_name = driver.find_element(
        By.CLASS_NAME, "modal-title").text.split("—")[0].strip()
    uni_country = driver.find_element(By.CLASS_NAME, "text-muted").text[2:]

    if len(uni_name) == 0:
        uni_name = "Unknown"
    if len(uni_country) == 0:
        uni_name = "Unknown"

    table_elements = driver.find_elements(By.TAG_NAME, "td")

    if (len(table_elements) == 0):
        continue
    count = 0

    for items in table_elements:
        count += 1
        if count % 4 == 1:
            exchange_course_code = items.text
        elif count % 4 == 2:
            exchange_course_title = items.text
        elif count % 4 == 3:
            hku_course_code = items.text.split("\t")[0].strip()
        else:
            hku_course_title = items.text
            new_row = {
                'University': uni_name,
                'University-Country': uni_country,
                'Exchange-Course-Code': exchange_course_code,
                'Exchange-Course-Title': exchange_course_title,
                'HKU-Course-Code': hku_course_code,
                'HKU-Course-Title': hku_course_title
            }
            df.loc[len(df)] = new_row

driver.quit()
print(df.head())
df.to_csv("business-credit_transfer_database.csv", index=False)
