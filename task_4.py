class EmployeeSalary:

    hourly_payment = 400

    def init(self, name, hours, rest_day, email):
        self.name = name
        self.hours = hours
        self.rest_day = rest_day
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - cls.rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, rest_days, hours):
        email = f"{cls.name}@email.com"
        return cls(name, hours, rest_days, email)

    def set_hourly_payment(self, payment):
        self.hourly_payment = payment

    def salary(self):
        return self.hours * self.hourly_payment
