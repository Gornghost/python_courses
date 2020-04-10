from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self, wd):
        wd.find_element_by_xpath("// a[contains(text(), 'LOGOUT')]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("HOME").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_xpath(contact.birthday_day).click()
        wd.find_element_by_xpath(contact.birthday_month).click()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_xpath(contact.anniversary_day).click()
        wd.find_element_by_xpath(contact.anniversary_month).click()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("ADD_NEW").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//body//input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd, Contact(first_name="test fname", middle_name="test mname", last_name="test lname", nickname="test nickname",
                                        title="test title", company="test company", address="test address",
                                        phone_home="test phone home", phone_mobile="test phone mobile", phone_work="test phone work", fax="test fax",
                                        email="test email", email2="test email 2", email3="test email 3", homepage="test homepage",
                                        birthday_day="//select[@name='bday']//option[3]", birthday_month="//select[@name='bmonth']//option[5]", birthday_year="2000",
                                        anniversary_day="//select[@name='aday']//option[3]", anniversary_month="//select[@name='amonth']//option[3]", anniversary_year="2000",
                                        secondary_address="test secondary address", secondary_phone="test secondary phone", secondary_notes="test secondary notes"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
