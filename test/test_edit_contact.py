from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    contact = Contact(first_name="EDITED", middle_name="EDITED", last_name="EDITED", nickname=" EDITED",
                               title=" EDITED", company=" EDITED", address="EDITED",
                               phone_home=" EDITED", phone_mobile=" EDITED", phone_work=" EDITED", fax=" EDITED",
                               email=" EDITED", email2=" EDITED", email3=" EDITED", homepage=" EDITED",
                               birthday_day="//select[@name='bday']//option[5]", birthday_month="//select[@name='bmonth']//option[7]", birthday_year="2020",
                               anniversary_day="//select[@name='aday']//option[3]", anniversary_month="//select[@name='amonth']//option[3]", anniversary_year="2000",
                               secondary_address=" EDITED", secondary_phone=" EDITED", secondary_notes=" EDITED")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)