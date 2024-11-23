from pages.home_page import HomePage
from utils.driver import get_driver

def test_home_navigation():
    driver = get_driver()
    home_page = HomePage(driver)

    home_page.load
    home_page.click_contact

    assert "Contact" in driver.title
    screenshot_path = "screenshot.png"
    driver.get_screenshot_as_file(screenshot_path)
    print(f"screenshot saved at {screenshot_path}")
    driver.quit