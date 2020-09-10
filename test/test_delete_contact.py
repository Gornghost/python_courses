from model.contact import Contact


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    index = app.random_element_of_list(old_contacts)
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.delete_all_contacts()
    assert len(app.contact.get_contact_list()) == 0