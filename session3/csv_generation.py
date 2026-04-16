import csv;
import random;
import string;

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

file_name = 'data/data_processing_XXL.csv'
num_rows = 50000000
header = ['id', 'name', 'email', 'age', 'country', 'signup_date', 'last_login']

with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for i in range(num_rows):
        name = generate_random_string()
        email = f'{name}@example.com'
        age = random.randint(18, 80)
        country = random.choice(['USA', 'Canada', 'UK', 'Australia'])
        signup_date = f'{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}'
        last_login = f'{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}'
        writer.writerow([i + 1, name, email, age, country, signup_date, last_login])
print(f'\'{file_name}\' with {num_rows} rows has been created.')