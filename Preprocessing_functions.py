# importing relevant helper functions for classes Vehicle, CreditCard, Address and Customer
from datetime import datetime

from helper_function import Vehicle, CreditCard, Address, Customer


# Function that does the error handling and type conversions
def process_row(row, csv_columns, row_num):
    # If the value is null and an error is raised, change the value in that cell to None
    # Print the result showing that there is an error in that row for that column

    age_value = row[csv_columns['age']]
    try:
        age = int(age_value) if age_value is not None and age_value != '' else None
    except ValueError:
        print(f'Error in row {row_num}, column age: {age_value} is not a valid integer')
        age = None

    retired_value = row[csv_columns['retired']]
    retired = str(retired_value).lower() == 'true'

    # Dependents column processing
    dependents_value = row[csv_columns['dependants']]
    try:
        if dependents_value is not None:
            dependants = int(dependents_value)
        else:
            dependants = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column dependants: {dependents_value} is not a valid integer')
        dependants = None

    # Salary column processing
    salary_value = row[csv_columns['salary']]
    try:
        if salary_value is not None:
            salary = int(salary_value)
        else:
            salary = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column salary')
        salary = None

    # Pension column processing
    pension_value = row[csv_columns['pension']]
    try:
        if pension_value is not None:
            pension = int(pension_value)
        else:
            pension = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column pension')
        pension = None

    # Commute distance column processing
    commute_distance_value = row[csv_columns['commute_distance']]
    try:
        if commute_distance_value is not None:
            commute_distance = float(commute_distance_value)
        else:
            commute_distance = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column commute_distance')
        commute_distance = None

    # Credit card number column processing
    number_value = row[csv_columns['number']]
    try:
        if number_value is not None:
            number = float(number_value)
        else:
            number = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column number')
        number = None

    # Credit card CVV column processing
    cvv_value = row[csv_columns['cvv']]
    try:
        if cvv_value is not None:
            cvv = float(cvv_value)
        else:
            cvv = None
    except (ValueError, TypeError):
        print(f'value error in row {row_num}, column cvv')
        cvv = None

    # Credit card start_date column processing
    start_date_value = row[csv_columns['start_date']]
    try:
        if start_date_value is not None and start_date_value != '':
            if len(start_date_value.split('-')[1]) == 2:  # Check if it's in the format 'Aug-18'
                start_date = start_date_value
            else:
                start_date_parts = start_date_value.split('-')
                start_date = start_date_parts[1] + '-' + start_date_parts[0]  # Switch order to '08-Dec'
        else:
            start_date = None
    except ValueError:
        print(f'value error in row {row_num}, column start_date')
        start_date = None

    # Credit card end_date column processing
    end_date_value = row[csv_columns['end_date']]
    try:
        if end_date_value is not None and end_date_value != '':
            if len(end_date_value.split('-')[1]) == 2:  # Check if it's in the format 'Aug-18'
                end_date = end_date_value
            else:
                end_date_parts = end_date_value.split('-')
                end_date = end_date_parts[1] + '-' + end_date_parts[0]  # Switch order to '08-Dec'
        else:
            end_date = None
    except ValueError:
        print(f'value error in row {row_num}, column end_date')
        end_date = None
    # Mapping the data
    vehicle = Vehicle(row[csv_columns['make']],
                      row[csv_columns['model']],
                      row[csv_columns['year']],
                      row[csv_columns['category']])

    credit_card = CreditCard(start_date,
                             end_date,
                             number,
                             cvv,
                             row[csv_columns['iban']])

    address = Address(row[csv_columns['street']],
                      row[csv_columns['city']],
                      row[csv_columns['postcode']])

    customer = Customer(row[csv_columns['first_name']],
                        row[csv_columns['last_name']],
                        age,
                        row[csv_columns['sex']],
                        retired,
                        row[csv_columns['marital_status']],
                        dependants,
                        salary,
                        pension,
                        row[csv_columns['company']],
                        commute_distance,
                        vehicle,
                        credit_card,
                        address).to_dict()

    return customer


# Function to accept a single row and then print out whether a customer should be flagged
# This is based on credit card start and end date
def flag_credit_card(row):
    try:
        start_date = row['credit_card']['start_date']
        end_date = row['credit_card']['end_date']

        if start_date is not None:
            start_date = datetime.strptime(start_date, '%b-%y')
        else:
            print('Start date is None')
            return 'Error_Flag_Card'

        if end_date is not None:
            end_date = datetime.strptime(end_date, '%b-%y')
        else:
            print('End date is None')
            return 'Error_Flag_Card'
    except ValueError as e:
        error_message = f"Error parsing date in credit card: {e}"
        print(error_message)
        return 'Error_Flag_Card'

    time_difference_days = (end_date - start_date).days
    years_calculated = time_difference_days / 365

    threshold_years = 10

    if years_calculated > threshold_years:
        return 'Flag_Card'
    else:
        return 'Do_Not_Flag_Card'
