from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# service = Service(executable_path="chromedriver.exe")
driver = webdriver.Safari()

driver.get("https://arts.hku.hk/ct-database/index.php")

df = pd.DataFrame(columns=[
    'University',
    'University-Country',
    'Exchange-Course-Code',
    'Exchange-Course-Title',
    'HKU-Course-Code',
    'HKU-Course-Title'
])

country_elems = driver.find_elements(By.XPATH, "//h4 [@id]")
country_names = []
num_universities_by_country = []

for country in country_elems:
    country_names.append(country.text)

multicols = driver.find_elements(By.CLASS_NAME, "multicol")
for universities in multicols:
    num_universities_by_country.append(
        len(universities.find_elements(By.TAG_NAME, "li")))


current_country = 1
count = 1

table_elements = driver.find_elements(By.CLASS_NAME, "modal-body")
for table_element in table_elements:
    cells = table_element.find_elements(By.TAG_NAME, "td")
    internal_count = 0

    for cell in cells:

        if internal_count % 4 == 0:
            uni_name = cell.text
        elif internal_count % 4 == 1:
            exchange_course_title = cell.text
        elif internal_count % 4 == 2:
            hku_course_code = cell.text
        else:
            new_row = {
                'University': uni_name,
                'University-Country': country_names[current_country - 1],
                'Exchange-Course-Code': "-",
                'Exchange-Course-Title': exchange_course_title,
                'HKU-Course-Code': hku_course_code,
                'HKU-Course-Title': "-"
            }
            df.loc[len(df)] = new_row
        internal_count += 1

    count += 1
    if (count > sum(num_universities_by_country[:current_country])):
        current_country += 1
driver.quit()

print(df)
df.to_csv("arts-credit_transfer_database.csv", index=False)
