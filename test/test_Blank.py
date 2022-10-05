import time

import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestBlankForm(BaseClass):
    @pytest.mark.run(order=1)
    def testBlankSubmit(self):
        self.driver.get("http://localhost:8000/wordpress/contact-me/")
        log = self.getLogger()
        print(self.driver.title)
        assert self.driver.title=="UI Automation With Selenium"
        print(self.driver.current_url)
        log.info("current url verified")
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/form[1]/div[12]/button[1]').click()
        time.sleep(3)
        message = self.driver.find_element(By.CLASS_NAME, "ff-message-success").text
        log.info("Text received from application is "+message)
        assert "Thank you for your messagess" in message