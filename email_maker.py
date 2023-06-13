import sys


# Check if the required arguments are provided
if len(sys.argv) < 4:
    print("Please provide the paths of the first names and last names text files as command-line arguments.")
    print("Please provide the domain used for the emails. ")
    print("Example usage: python3 email_maker.py /path/to/first_names.txt /path/to/last_names.txt " "email.com")
    sys.exit(1)

first_names_file = sys.argv[1]
last_names_file = sys.argv[2]
email_domain = sys.argv[3]

# Read first names from the specified text file
with open(first_names_file, 'r') as f:
    first_names_file = f.read().splitlines()

# Read last names from the specified text file
with open(last_names_file, 'r') as f:
    last_names = f.read().splitlines()

email_addresses = []
for first_name in first_names_file:
    for last_name in last_names:
        email = f"{first_name.lower()}.{last_name.lower()}@{email_domain}"
        email_addresses.append(email)

for email in email_addresses:
    print(email)