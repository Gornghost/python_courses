from model.contact import Contact
import time
import re


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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion in the pop up
        wd.switch_to_alert().accept()
        time.sleep(.1)  # I don't know why, but sometimes tests are down without this pause
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_edit_contact_page_by_index(index)
        # edit contact form
        self.fill_contact_form(contact)
        # click Update
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_edit_contact_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click "edit"
        wd.find_element_by_xpath("//table[@id='maintable']//tr[@name='entry'][%s]/td[8]/a/img" % str(index+1)).click()

    # def click_on_edit_icon_by_index(self, index):
    #     wd = self.app.wd
    #     contact = wd.find_elements_by_name("entry")[index]
    #     contact.find_element_by_xpath(".//td[8]/a/img")

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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                contact_id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_contact_page_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, contact_id=contact_id, phone_home=phone_home,
                       phone_mobile=phone_mobile, phone_work=phone_work, secondary_phone=secondary_phone)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_page_by_index(index)
        full_text = wd.find_element_by_id("content").text
        # phone_home = re.search("H: (.*)", full_text).group(1)
        phone_home = self.find_by_text_and_get_value("H: ", full_text)
        phone_mobile = self.find_by_text_and_get_value ("M: ", full_text)
        phone_work = self.find_by_text_and_get_value ("W: ", full_text)
        secondary_phone = self.find_by_text_and_get_value ("P: ", full_text)
        return Contact(phone_home=phone_home,phone_mobile=phone_mobile, phone_work=phone_work, secondary_phone=secondary_phone)

    def find_by_text_and_get_value(self, searching_text, full_text):
        if re.search(searching_text, full_text):
            return re.search("%s(.*)" % searching_text, full_text).group(1)
        else:
            return ""

    def open_view_contact_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click "edit"
        wd.find_element_by_xpath("//table[@id='maintable']//tr[@name='entry'][%s]/td[7]/a/img" % str(index+1)).click()