from faker import Faker

fake = Faker()

def generate_user():
    email = fake.email()
    password = fake.password()
    name = fake.name()
    user_data = {
        'email': email,
        'password': password,
        'name': name
         }
    return user_data

def generate_user_no_email():
    password = fake.password()
    name = fake.name()
    user_data_no_email = {
        'email': '',
        'password': password,
        'name': name
         }
    return user_data_no_email

def generate_user_no_password():
    email = fake.email()
    name = fake.name()
    user_data_no_password = {
        'email': email,
        'password': '',
        'name': name
        }
    return user_data_no_password

def generate_user_no_name():
    email = fake.email()
    password = fake.password()
    user_data_no_name = {
        'email': email,
        'password': password,
        'name': ''
        }
    return user_data_no_name