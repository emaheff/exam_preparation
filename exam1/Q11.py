class Date:

    def __init__(self, d, m, y):
        self._day = d
        self._month = m
        self._year = y

    def get_day(self): return self._day
    def get_month(self): return self._month
    def get_year(self): return self._year
    def set_day(self, day): self._day = day
    def set_month(self, month): self._month = month
    def set_year(self, year): self._year = year

    def __str__(self):
        return f"({self._day}.{self._month}.{self._year}"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self._year == other._year and self._month == other._month and self._day == other._day
        return NotImplemented

    def __it__(self, other):
        if self._year < other.get_year():
            return True
        elif self._year == other.get_year() and self._month < other.get_month():
            return True
        elif self._year == other.get_year() and self._month == other.get_month() and self._day < other.get_day():
            return True
        return False


class Person:

    def __init__(self, name, id, b_day):
        self._name = name
        self._id = id
        self._birth = b_day

    def get_name(self): return self._name
    def get_id(self): return self._id
    def get_birth(self): return self._birth
    def set_name(self, name): self._name = name
    def set_id(self, id): self._id = id
    def set_birth(self, birth): self._birth = birth

    def __str__(self):
        return f"name: {self._name}\nid: {self._id}\nbirth day: {self._birth}"

    def __eq__(self, other):
        return self._name == other.get_name() and self._birth == other.get_birth()


class ContactList:

    def __init__(self):
        self._contacts = []

    def add_contact(self, contact):
        self._contacts.append(contact)

    def born_in_date(self, d):
        res = 0

        for contact in self._contacts:
            if contact.get_birth() == d:
                res += 1

        return res

    def oldest_contact(self):
        if not self._contacts:
            return None

        oldest = self._contacts[0].get_birth()
        name = self._contacts[0].get_name()

        for contact in self._contacts:
            if contact.get_birth() < oldest:
                oldest = contact.get_birth()
                name = contact.get_name()

        return name

    def born_in_month(self):
        if not self._contacts:
            return None

        month_count = [0 for _ in range(12)]

        for contact in self._contacts:
            month = contact.get_birth().get_month()
            month_count[month-1] += 1

        res = []
        for i in range(len(month_count)):
            if month_count[i] != 0:
                res.append((i + 1, month_count[i]))

        return res
