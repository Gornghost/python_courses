from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="test fname", middle_name="test mname", last_name="test lname", nickname="test nickname",
                               title="test title", company="test company", address="test address",
                               phone_home="test phone home", phone_mobile="test phone mobile", phone_work="test phone work", fax="test fax",
                               email="test email", email2="test email 2", email3="test email 3", homepage="test homepage",
                               birthday_day="//select[@name='bday']//option[3]", birthday_month="//select[@name='bmonth']//option[5]", birthday_year="2000",
                               anniversary_day="//select[@name='aday']//option[3]", anniversary_month="//select[@name='amonth']//option[3]", anniversary_year="2000",
                               secondary_address="test secondary address", secondary_phone="test secondary phone", secondary_notes="test secondary notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)