from faker import Faker
import json

# Initialize Faker
fake = Faker()

# Function to generate a single fake user record
def generate_fake_user():
    return {
        "id": fake.uuid4(),  # Unique ID
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job_title": fake.job(),
        "company": fake.company(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
        "profile_summary": fake.paragraph(nb_sentences=3)
    }

# Generate a list of multiple fake user records
num_records = 10
fake_data = [generate_fake_user() for _ in range(num_records)]

# Define the output filename
output_filename = "fake_users_data.json"

# Save the data to a JSON file
try:
    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(fake_data, json_file, indent=4, ensure_ascii=False)
    print(f"Successfully generated '{num_records}' fake user records and saved to '{output_filename}'")
except IOError as e:
    print(f"Error writing to file: {e}")