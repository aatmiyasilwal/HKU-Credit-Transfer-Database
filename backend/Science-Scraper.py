from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Safari()

df = pd.DataFrame(columns=[
    'University',
    'University-Country',
    'Exchange-Course-Code',
    'Exchange-Course-Title',
    'HKU-Course-Code',
    'HKU-Course-Title'
])

count = 0
driver.get("https://webapp.science.hku.hk/student/servlet/course_equiv")

init = Select(driver.find_element(By.NAME, "ex_ucode"))
options = init.options
count = len(options) - 1

while count >= 0:
    driver.get("https://webapp.science.hku.hk/student/servlet/course_equiv")
    curr_elem_node = Select(driver.find_element(By.NAME, "ex_ucode"))
    curr_option = curr_elem_node.options[count]
    val = curr_option.get_attribute("value")

    if val:
        info = curr_option.text
        country_start, country_end = curr_option.text.index(
            ".") + 2, curr_option.text.index("-") - 1
        curr_elem_node.select_by_value(val)
        time.sleep(2)

        table_rows = driver.find_elements(
            By.XPATH, "//table[@class='msg']/tbody/tr")
        for row in table_rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "\n\t\t":
                break
            new_row = {
                'University': info[country_end + 2:].strip(""),
                'University-Country': info[country_start:country_end].strip(),
                'Exchange-Course-Code': cells[1].text.strip(),
                'Exchange-Course-Title': cells[3].text.strip(""),
                'HKU-Course-Code': cells[4].text.strip(),
                'HKU-Course-Title': cells[6].text.strip()
            }
            df.loc[len(df)] = new_row
    count -= 1

driver.quit()
df.to_csv("science-credit_transfer_database.csv", index=False)
