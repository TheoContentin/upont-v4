from django.contrib.auth import models
from django.test import TestCase, tag
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTest(TestCase):
    def setUp(self):
        self.firefox = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX,
        )

    @tag("selenium")
    def test_login_with_chrome(self):
        browser = self.firefox
        test_user = models.User(username="user1", password="secret_password")
        test_user.save()
        browser.get("http://back:8000/login/")
        username_input = browser.find_element_by_name("username")
        username_input.send_keys("user1")
        password_input = browser.find_element_by_name("password")
        password_input.send_keys("secret_password")
        browser.find_element_by_xpath('//input[@value="Se connecter"]').click()

    def tearDown(self):
        self.firefox.quit()
