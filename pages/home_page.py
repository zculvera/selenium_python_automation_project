from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://automationintesting.online/"
    CONTACT_BUTTON = (By.ID, "contact")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def click_contact(self):
        self.driver.find_element(*self.CONTACT_BUTTON).click()
        