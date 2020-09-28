from model.contact import Contact
import random
import string
import os.path
import jsonpickle


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


def random_email(prefix):
    symbols_before_at = string.ascii_letters + string.digits + "."*10
    symbols_after_at = string.ascii_letters + string.digits
    domain = string.ascii_letters
    return prefix + "".join([random.choice(symbols_before_at) for i in range(random.randrange(1, 10))]) + \
           "@" + "".join([random.choice(symbols_after_at) for i in range(random.randrange(1, 10))]) + \
           "." + "".join([random.choice(domain) for i in range(random.randrange(2, 5))])


phone_codes = ["+380", "+375", "+44", "+1", "+46", "+49"]


def random_phone():
    symbols = string.digits + "(" + ")" + "-"
    random_phone_code = phone_codes[random.randrange(len(phone_codes))]
    return random_phone_code + "".join([random.choice(symbols) for i in range(random.randrange(4, 15))])


def random_day(field):
    return "//select[@name='%s']//option[%s]" % (field, random.randrange(3, 34))


def random_month(field):
    return "//select[@name='%s']//option[%s]" % (field, random.randrange(2, 14))


def random_year():
    return random.randrange(1990, 2020)


testdata = [
    Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("fname_", 10), middle_name=random_string("mname_", 10),
            last_name=random_string("lname_", 20), nickname=random_string("nickname_", 15),
            title=random_string("title_", 10), company=random_string("company_", 20),
            address=random_string("address_", 50), phone_home=random_phone(),
            phone_mobile=random_phone(), phone_work=random_phone(), fax=random_phone(), email=random_email("email_"),
            email2=random_email("email2_"), email3=random_email("email3_"), homepage=random_string("homepage_", 20),
            birthday_day=random_day("bday"), birthday_month=random_month("bmonth"),
            birthday_year=random_year(), anniversary_day=random_day("aday"),
            anniversary_month=random_month("amonth"), anniversary_year=random_year(),
            secondary_address=random_string("secondary_address_", 50), secondary_phone=random_phone(),
            secondary_notes=random_string("notes_", 250))
    for i in range(10)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))