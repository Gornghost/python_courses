from application import Application
import pytest
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_contact(Contact(first_name="test fname", middle_name="test mname", last_name="test lname", nickname="test nickname",
                                    title="test title", company="test company", address="test address",
                                    phone_home="test phone home", phone_mobile="test phone mobile", phone_work="test phone work", fax="test fax",
                                    email="test email", email2="test email 2", email3="test email 3", homepage="test homepage",
                                    birthday_day="//select[@name='bday']//option[3]", birthday_month="//select[@name='bmonth']//option[5]", birthday_year="2000",
                                    anniversary_day="//select[@name='aday']//option[3]", anniversary_month="//select[@name='amonth']//option[3]", anniversary_year="2000",
                                    secondary_address="test secondary address", secondary_phone="test secondary phone", secondary_notes="test secondary notes"))
    app.return_to_homepage()
    app.logout()