from selenium.webdriver.common.by import By

class ContactPage:
    NAME_INPUT = (By.ID,"name")
    EMAIL_INPUT = (By.ID,"email")
    MESSAGE_INPUT = (By.ID,"message")
    SUBMIT_BUTTON = (By.ID,"submitContact")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, name, email, message):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()