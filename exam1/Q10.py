class Time:

    def __init__(self, h=0, m=0):
        self._hour = h
        self._minute = m

    def set_hour(self, hour):
        self._hour = hour

    def set_minute(self, minute):
        self._minute = minute

    def get_hour(self):
        return self._hour

    def get_minute(self):
        return self._minute

    def __str__(self):
        return f"({self._hour}:{self._minute})"


class Date:

    def __init__(self, d, m, y):
        self._day = d
        self._month = m
        self._year = y

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

    def set_day(self, day):
        self._day = day

    def set_month(self, month):
        self._month = month

    def set_year(self, year):
        self._year = year

    def __str__(self):
        return f"({self._day}.{self._month}.{self._year}"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self._year == other.get_year() and self._month == other.get_month() and self._day == other.get_day()
        return NotImplemented


class Order:
    _order_num = 1

    def __init__(self, day, month, year, hour, minute, cost=50):
        date = Date(day, month, year)
        time = Time(hour, minute)
        self._t = time
        self._d = date
        self._order_id = Order._order_num
        Order._order_num += 1
        self._cost = cost

    def set_time(self, time):
        self._t = time

    def set_date(self, date):
        self._d = date

    def set_cost(self, cost):
        self._cost = cost

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_time(self):
        return self._t

    def get_date(self):
        return self._d

    def get_cost(self):
        return self._cost

    def get_order_id(self):
        return self._order_id

    def __str__(self):
        return f"Order num {self._order_id}. date: {self._d}. time: {self._t}. cost: {self._cost}"

    def __gt__(self, other):
        if isinstance(other, Order):
            return other.get_cost() > self._cost
        return NotImplemented


class CashRegister:

    def __init__(self):
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def monthly_total_income(self, month):
        income = 0
        for order in self._orders:
            if order.get_date().get_month() == month:
                income += order.get_cost()
        return income

    def most_expensive_order(self, date):
        most_ex = 0
        order_id = 0
        for order in self._orders:
            if order.get_date() == date:
                most_ex = order.get_cost()
                order_id = order.get_order_id()
                break
        for order in self._orders:
            if order.get_date() == date:
                if order.get_cost() > most_ex:
                    most_ex = order.get_cost()
                    order_id = order.get_order_id()

        return order_id

    def less_than(self, cost):
        res = []
        for order in self._orders:
            if order.get_cost() < cost:
                res.append(order)

        if len(res) == 0:
            return None
        return res
