from pages.contact_page import ContactPage
from utils.driver import get_driver

def test_contact_form_submission():
    driver = get_driver()
    contact_page = ContactPage(driver)

    contact_page.fill_form("John Doe", "john.doe@example.com", "Hello, this is a test message.")
    contact_page.submit_form()

    screenshot_path = "screenshot.png"
    driver.get_screenshot_as_file(screenshot_path)
    print(f"screenshot saved at {screenshot_path}")