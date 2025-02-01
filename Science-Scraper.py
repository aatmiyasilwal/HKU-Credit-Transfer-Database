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

select_element = Select(driver.find_element(By.NAME, "ex_ucode"))
options = select_element.options

count = len(options) - 1

while count >= 0:
    driver.get("https://webapp.science.hku.hk/student/servlet/course_equiv")
    curr_elem_node = Select(driver.find_element(By.NAME, "ex_ucode"))
    curr_option = curr_elem_node.options[count]
    val = curr_option.get_attribute("value")

    if val:  
        curr_elem_node.select_by_value(val)  
        time.sleep(2)
    
        table_rows = driver.find_elements(By.XPATH, "//table[@class='msg']/tbody/tr")
        for row in table_rows[1:]:  # Skip header row
            cells = row.find_elements(By.TAG_NAME, "td")
            print([cell.text for cell in cells])
    
    print("*" * 20)
    
    count -= 1

driver.quit()