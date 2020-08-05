from model.contact import Contact
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_list_value(contact.birthday_day)
        self.change_select_list_value(contact.birthday_month)
        self.change_field_value("byear", contact.birthday_year)
        self.change_select_list_value(contact.anniversary_day)
        self.change_select_list_value(contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("notes", contact.secondary_notes)

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("ADD_NEW").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion in the pop up
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # click "edit"
        wd.find_element_by_xpath("//table[@id='maintable']//tr[@name='entry'][1]/td[8]").click()
        # edit contact form
        self.fill_contact_form(contact)
        # click Update
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def change_field_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def change_select_list_value(self, select_list):
        wd = self.app.wd
        if select_list is not None:
            wd.find_element_by_xpath(select_list).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.app.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            time.sleep(.050)    # I don't know why, but sometimes tests are down without this pause
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                last_name = element.find_element_by_xpath("./td[2]").text
                first_name = element.find_element_by_xpath("./td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.contact_cache)