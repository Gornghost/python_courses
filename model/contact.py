from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None,
                 secondary_address=None, secondary_phone=None, secondary_notes=None, contact_id=None, all_phones_from_homepage=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.secondary_notes = secondary_notes
        self.contact_id = contact_id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)

    def __repr__(self):
        return "%s: %s, %s" % (self.contact_id, self.first_name, self.last_name)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize