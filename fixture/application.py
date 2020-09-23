from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from random import randrange


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.get(self.base_url)

    def return_to_homepage(self):
        wd = self.wd
        if not self.current_page_is_homepage():
            wd.find_element_by_link_text("HOME").click()

    def random_element_of_list(self, list_items):
        return randrange(len(list_items))

    def current_page_is_homepage(self):
        wd = self.wd
        return (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_name("MainForm")) > 0 and
                len(wd.find_elements_by_name("group")) > 0)

    def destroy(self):
        self.wd.quit()