import os
from dotenv import load_dotenv
import random
from faker import Faker


load_dotenv()

class Data:

    _instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Data, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.fake = Faker()
            self.email = self.generate_random_email()
            self.login_name = self.fake.name()
            self.password = 'password123qwerty'
            self.first_name = self.fake.first_name()
            self.last_name = self.fake.last_name()
            self.company = self.fake.company()
            self.street_address = self.fake.street_address()
            self.secondary_address = self.fake.secondary_address()
            self.country = 'Canada'
            self.state = self.fake.state()
            self.city = self.fake.city()
            self.zipcode = self.fake.zipcode()
            self.phone_number = self.fake.phone_number()
            self.birth_day = str(self.fake.random_int(min=1, max=31))
            self.birth_month = self.fake.month_name()
            self.birth_year = str(self.fake.random_int(min=1900, max=2021))
            self.expiration_year = str(self.fake.random_int(min=1900, max=2021))
            self.expiration_month = str(self.fake.random_int(min=1, max=12)).zfill(2)
            self.card_cvc = str(self.fake.random_int(min=1, max=999)).zfill(3)
            self.credit_card_number = self.fake.credit_card_number(card_type=None)
            self.credit_card_name = f'{self.first_name} {self.last_name}'
            self._initialized = True

    def generate_random_email(self):
        random_number = random.randint(0, 9999)
        return f"testmail{random_number}@mail.com"
