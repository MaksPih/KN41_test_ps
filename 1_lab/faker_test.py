from faker import Faker

fake = Faker()

print("Ім'я:", fake.name())
print("Email:", fake.email())
print("Адреса:", fake.address())