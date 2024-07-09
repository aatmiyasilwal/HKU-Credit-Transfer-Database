from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Safari()
driver.get("https://webapp.science.hku.hk/student/servlet/course_equiv")

df = pd.DataFrame(columns=[
    'University',
    'University-Country',
    'Exchange-Course-Code',
    'Exchange-Course-Title',
    'HKU-Course-Code',
    'HKU-Course-Title'
])

options = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "option")))

for option in options:
    value = option.get_attribute("value")
    print(value)

    if value == "":
        continue

    # Select the option
    option.click()

    # Wait for the table to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Extract university name and country
    #current_uni = option.text.split(" - ")[1]
    #uni_country = option.text.split(". ")[1].split(" - ")[0]

    # Get all table rows
    rows = driver.find_elements(By.TAG_NAME, "tr")  # Find rows directly without using table reference

    # Skip the header row and the last row (empty)
    rows = rows[1:-1]

    for row in rows:
        # Find the cells again after the page reloads
        cells = row.find_elements(By.TAG_NAME, "td")

        # Create a new row dictionary
        new_row = {
            'University': "current_uni",
            'University-Country': "uni_country",
            'Exchange-Course-Code': cells[1].text,  # Index 1 for "Partner Code"
            'Exchange-Course-Title': cells[3].text,  # Index 3 for "Partner Title"
            'HKU-Course-Code': cells[4].text,  # Index 4 for "HKU Code"
            'HKU-Course-Title': cells[5].text  # Index 5 for "HKU Title"
        }

        # Append the new row to the DataFrame
        df.loc[len(df)] = new_row

print(df)

driver.quit()

#df.to_csv("science-credit_transfer_database.csv", index=False)