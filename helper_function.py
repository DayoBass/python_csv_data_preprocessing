# import relevant libraries
import csv
from datetime import datetime


# Creating classes for the variables of each customer
# Vehicles have similar variables such as make, model, year and category and will be grouped together
class Vehicle:
    def __init__(self, make, model, year, vehicle_category):
        self.make = make
        self.model = model
        self.year = year
        self.category = vehicle_category

    # mapping vehicles to dictionary
    def to_dict(self):
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'category': self.category}


# Creating the credit card class
class CreditCard:
    def __init__(self, start_date, end_date, number, cvv, iban):
        self.start_date = start_date
        self.end_date = end_date
        self.number = number
        self.cvv = cvv
        self.iban = iban

    # mapping credit card details
    def to_dict(self):
        return {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number': self.number,
            'cvv': self.cvv,
            'iban': self.iban}


# Creating address class with variables such as address, city and postcode
class Address:
    def __init__(self, street, city, postcode):
        self.street = street
        self.city = city
        self.postcode = postcode

    # mapping address variables to dict
    def to_dict(self):
        return {
            'street': self.street,
            'city': self.city,
            'postcode': self.postcode}


# Final class which contains all variables for a customer
class Customer:
    def __init__(
        self,
        first_name,
        last_name,
        age,
        sex,
        retired,
        marital_status,
        dependants,
        salary,
        pension,
        company,
        commute_distance,
        vehicle,
        credit_card,
        address,

    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.retired = retired
        self.marital_status = marital_status
        self.dependants = dependants
        self.salary = salary
        self.pension = pension
        self.company = company
        self.commute_distance = commute_distance
        self.vehicle = vehicle
        self.credit_card = credit_card
        self.address = address

    # mapping all customer variables to dictionary
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'sex': self.sex,
            'retired': self.retired,
            'marital_status': self.marital_status,
            'dependants': self.dependants,
            'salary': self.salary,
            'pension': self.pension,
            'company': self.company,
            'commute_distance': self.commute_distance,
            'vehicle': self.vehicle.to_dict(),
            'credit_card': self.credit_card.to_dict(),
            'address': self.address.to_dict()}


# Function to read csv files
def read_csv(filepath, csv_columns):
    rows = []
    try:
        with open(filepath, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # print("Row read from CSV:", row)
                rows.append(row)
    except FileNotFoundError:
        print('File not found')
    return rows


def parse_date(date_str):
    try:
        # Try parsing as '%b-%y' format (e.g., 'Aug-18')
        return datetime.strptime(date_str, '%b-%y')
    except ValueError:
        try:
            # Try parsing as '%m-%y' format (e.g., '08-Dec')
            return datetime.strptime(date_str, '%m-%y')
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None
