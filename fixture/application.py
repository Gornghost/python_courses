from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not self.current_page_is_homepage():
            wd.get("http://localhost/addressbook")

    def return_to_homepage(self):
        wd = self.wd
        if not self.current_page_is_homepage():
            wd.find_element_by_link_text("HOME").click()

    def current_page_is_homepage(self):
        wd = self.wd
        return (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_name("MainForm")) > 0 and
                len(wd.find_elements_by_name("group")) > 0)

    def destroy(self):
        self.wd.quit()