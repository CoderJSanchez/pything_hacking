import sys


# Check if the required arguments are provided
if len(sys.argv) < 5:
    print("Please provide the paths of the first names and last names text files as command-line arguments.")
    print("Please provide the domain used for the emails. ")
    print("Please provide a name for your new out put file. ")
    print("Example usage: python3 email_maker.py /path/to/first_names.txt /path/to/last_names.txt email.com new_list.txt")
    sys.exit(1)

first_names_file = sys.argv[1]
last_names_file = sys.argv[2]
email_domain = sys.argv[3]
output_file = sys.argv[4]

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


# Saving the new email list
with open(output_file, 'w') as f:
    for email in email_addresses:
        f.write(email + '\n')

print(f"Email addresses saved to {output_file}")