import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#browser invocation
service_obj = Service("/Users/masiur/Desktop/Selenium/geckodriver")
driver = webdriver.Firefox(service=service_obj)

# service_obj = Service("/Users/masiur/Desktop/Selenium/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# service_obj = Service("/Users/masiur/Desktop/Selenium/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

#browser maximization
driver.maximize_window()

#Implicite wait
driver.implicitly_wait(15)

#Explicite wait
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located(By.XPATH, 'class_name'))

#scroll
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#UI operations
driver.get("http://localhost:8000/wordpress/contact-me/")
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, 'ff_3_names_first_name_').send_keys("Sarkar")
driver.find_element(By.ID, 'ff_3_names_last_name_').send_keys("Ripon")
driver.find_element(By.ID, 'ff_3_email').send_keys("me@sarkarripon.com")

time.sleep(3)
driver.find_element(By.ID, 'ff_3_address_1_address_line_1_').send_keys("Elahi 8B, Khuliapara")
driver.find_element(By.ID, 'ff_3_address_1_address_line_2_').send_keys("Surma gate")
driver.find_element(By.ID, 'ff_3_address_1_city_').send_keys("Sylhet")
driver.find_element(By.ID, 'ff_3_address_1_state_').send_keys("Sylhet")
driver.find_element(By.ID, 'ff_3_address_1_zip_').send_keys("3100")
time.sleep(3)
drpCountry = Select(driver.find_element(By.ID, 'ff_3_address_1_country_'))
drpCountry.select_by_visible_text('Bangladesh')
time.sleep(3)
driver.find_element(By.ID, 'ff_3_url').send_keys("https://www.sarkarripon.com/")
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[6]/div[2]/div[3]/label[1]/input[1]').click()
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[7]/div[2]/div[1]/label[1]/input[1]').click()
time.sleep(3)
drpCountry = Select(driver.find_element(By.ID, 'ff_3_dropdown'))
drpCountry.select_by_visible_text('Option 2')
time.sleep(3)
driver.find_element(By.ID, 'ff_3_datetime').click()
driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span[33]').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[10]/div[2]/div[1]/div[1]/input[1]').click()
driver.find_element(By.ID, 'choices--ff_3_multi_select-item-choice-2').click()
driver.find_element(By.ID, 'choices--ff_3_multi_select-item-choice-3').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[11]/div[2]/input[1]').send_keys('I dont know what to write here')
time.sleep(3)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[12]/button[1]').click()


driver.close()
