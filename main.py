import random
from faker import Faker

random_name=Faker().name()
random_birthday = Faker().date_of_birth().strftime('%Y-%m-%d')
random_address = Faker().address()
random_country = Faker().country()
random_job = Faker().job()
random_email = Faker().email()

print("Full Name :",random_name)
print("date of birth :",random_birthday)
print("address :",random_address)
print("country :",random_country)
print("job :",random_job)
print("e-mail :",random_email)
