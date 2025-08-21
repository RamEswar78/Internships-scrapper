from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)  # 👈 Keeps browser open
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.internshala.com/internships")

sleep(3)  # Wait for the browser to open

driver.find_element("id", "close_popup").click()  # Close the popup
sleep(3)  # Wait for the dropdown to open
options = ["Agent", "Web Development", "backend", "front end","full stack", "python", "javascript","artificial intelligence","software development"]

for i in options:
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "select_category_chosen"))).click()
        input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='select_category_chosen']//input")))

        input.send_keys(i+"\n")
        sleep(4)  # Wait for the dropdown to update
    # input.send_keys("\n")  # Select the first option
    except Exception as e:
        print(e)