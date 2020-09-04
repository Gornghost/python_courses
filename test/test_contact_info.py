import re


def test_contact_info_on_homepage(app):
    contact_list = app.contact.get_contact_list()
    index = app.random_element_of_list(contact_list)
    contact_from_homepage = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.first_name == contact_from_edit_page.first_name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_list = app.contact.get_contact_list()
    index = app.random_element_of_list(contact_list)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_view_page.phone_home) == clear(contact_from_edit_page.phone_home)
    assert clear(contact_from_view_page.phone_mobile) == clear(contact_from_edit_page.phone_mobile)
    assert clear(contact_from_view_page.phone_work) == clear(contact_from_edit_page.phone_work)
    assert clear(contact_from_view_page.secondary_phone) == clear(contact_from_edit_page.secondary_phone)


def clear(value):
    return re.sub("[() -]", "", value)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.secondary_phone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x.strip(),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))