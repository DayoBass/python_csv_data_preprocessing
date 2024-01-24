# File paths for input and output files
customer_file = r".\input_data\acw_user_data.csv"

# File path
filepath = customer_file

"""
- Giving the columns new names where necessary because some of the names such as Yearly Salary (GBP) are not helpful
- The new names will allow for easy imputing
"""
# column names for the csv
csv_columns = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'age': 'Age (Years)',
    'sex': 'Sex',
    'retired': 'Retired',
    'marital_status': 'Marital Status',
    'dependants': 'Dependants',
    'salary': 'Yearly Salary (GBP)',
    'pension': 'Yearly Pension (GBP)',
    'company': 'Employer Company',
    'commute_distance': 'Distance Commuted to Work (miles)',
    'make': 'Vehicle Make',
    'model': 'Vehicle Model',
    'year': 'Vehicle Year',
    'category': 'Vehicle Type',
    'start_date': 'Credit Card Start Date',
    'end_date': 'Credit Card Expiry Date',
    'number': 'Credit Card Number',
    'cvv': 'Credit Card CVV',
    'iban': 'Bank IBAN',
    'street': 'Address Street',
    'city': 'Address City',
    'postcode': 'Address Postcode'}
