import time
import pytest
from mailchimp3 import MailChimp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("setup")
class TestContactForm(BaseClass):
    @pytest.mark.run(order=2)
    def testUrlVerify(self):
        self.driver.get("http://localhost:8000/wordpress/contact-me/")
        log = self.getLogger()
        print(self.driver.title)
        assert self.driver.title=="UI automation With Selenium"
        print(self.driver.current_url)
        log.info("current url verified")

    @pytest.mark.run(order=3)
    def testFormData(self):
        log = self.getLogger()
        self.driver.find_element(By.ID, 'ff_3_names_first_name_').send_keys("Sarkar")
        self.driver.find_element(By.ID, 'ff_3_names_last_name_').send_keys("Ripon")
        self.driver.find_element(By.ID, 'ff_3_email').send_keys("dxbhgvdg@sarkarripon.com")
        log.info("first name, last name and email inserted")

        time.sleep(1)
        self.driver.find_element(By.ID, 'ff_3_address_1_address_line_1_').send_keys("Elahi 8B, Khuliapara")
        self.driver.find_element(By.ID, 'ff_3_address_1_address_line_2_').send_keys("Surma gate")
        self.driver.find_element(By.ID, 'ff_3_address_1_city_').send_keys("Sylhet")
        self.driver.find_element(By.ID, 'ff_3_address_1_state_').send_keys("Sylhet")
        self.driver.find_element(By.ID, 'ff_3_address_1_zip_').send_keys("3100")
        log.info("Address field data inserted")

        drpCountry = Select(self.driver.find_element(By.ID, 'ff_3_address_1_country_'))
        drpCountry.select_by_visible_text('Bangladesh')
        log.info("Country selected")
        time.sleep(1)
        self.driver.find_element(By.ID, 'ff_3_url').send_keys("https://www.sarkarripon.com/")
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[6]/div[2]/div[3]/label[1]/input[1]').click()
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[7]/div[2]/div[1]/label[1]/input[1]').click()
        log.info("Website url inserted")
        time.sleep(1)
        drpCountry = Select(self.driver.find_element(By.ID, 'ff_3_dropdown'))
        drpCountry.select_by_visible_text('Option 2')
        log.info("Item selected from dropdown menu")
        time.sleep(1)
        self.driver.find_element(By.ID, 'ff_3_datetime').click()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span[33]').click()
        log.info("Date picked")
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[10]/div[2]/div[1]/div[1]/input[1]').click()
        log.info("multiple items selected")
        self.driver.find_element(By.ID, 'choices--ff_3_multi_select-item-choice-2').click()
        self.driver.find_element(By.ID, 'choices--ff_3_multi_select-item-choice-3').click()

        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[11]/div[2]/input[1]').send_keys('I dont know what to write here')
        log.info("Musk input inserted")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[12]/button[1]').click()
        time.sleep(3)
        message = self.driver.find_element(By.CLASS_NAME, "ff-message-success").text
        log.info("Text received from application is "+message)
        assert "Thank you for your message" in message