# Importing relevant modules
import os
import json
from Preprocessing_functions import process_row, flag_credit_card
from helper_function import read_csv
from constants import csv_columns, filepath


# function to process the csv
def process_csv(file, csv):
    # creating an output_folder for the data
    if not os.path.exists(file):
        print(f"File {filepath} not found!")
        return None

    # relevant lists which hold the data
    # using the function created earlier to read the csv file
    rows = read_csv(file, csv)
    customers = []
    problematic_rows = []
    retired_data = []
    employed_data = []
    remove_ccard = []

    # The row_num variable from process_row function
    row_num = 0
    for row in rows:
        row_num += 1

        # using the function created to process the rows
        customer = process_row(row, csv_columns, row_num)
        customers.append(customer)

        # I have done this for the dependants column because it is mentioned in the brief to contain errors for certain
        # In another case, this code will be repeated for the other error handling defined in the function for row
        if customer['dependants'] is None:
            customer['dependants'] = 0
            problematic_rows.append(row_num)

    # This prints out the rows where there are problems in the dependants column
    if problematic_rows:
        print(f"\nProblematic rows for dependants: {problematic_rows}\n")

    # The plan is to store the output json files in a folder called output_data
    # The code below checks if the output_data folder has been created
    # If it has not been created, it is then created
    if not os.path.exists('output_data'):
        os.makedirs('output_data')

    # Write data to json file
    with open('output_data/processed.json', 'w') as processed_json:
        json.dump(customers, processed_json)

    # The code below answers one of the questions relating to retired and employed
    # It checks whether as indicated by the retired field, if it is true then retired_data
    # If the company is not N/A then employed_data
    for customer in customers:
        if customer['retired']:
            retired_data.append(customer)
        if customer['company'] != 'N/A':
            employed_data.append(customer)

    # Write data to json file
    with open('output_data/retired.json', 'w') as retired_json:
        json.dump([customer for customer in retired_data], retired_json)

    # Write data to json file
    with open('output_data/employed.json', 'w') as employed_json:
        json.dump([customer for customer in employed_data], employed_json)

    # The cell which contains the Flag_Credit_Card function
    # This function is supposed to flag rows where the start_date and end-date is more than 10 years
    for customer in customers:
        if flag_credit_card(customer) == 'Flag_Card':
            remove_ccard.append(customer)

    # Write data to json file
    with open('output_data/remove_ccard.json', 'w') as remove_ccard_json:
        json.dump([customer for customer in remove_ccard], remove_ccard_json)

    # print to confirm the length of the different lists. This is for validation purposes
    # print to confirm that the json file has been created after the code runs
    if customers:
        print(f"{'processed.json'} has been created in output_data folder!")
        print('Number of customers in customers data (processed.json):', len(customers))
        print('\n')
    else:
        print('There is an error and processed.json was not created')
        print('\n')

    if retired_data:
        print(f"{'retired.json'} has been created in output_data folder!")
        print('Number of customers in retired data (retired.json):', len(retired_data))
        print('\n')
    else:
        print('There is an error and retired.json was not created')
        print('\n')

    if employed_data:
        print(f"{'employed.json'} has been created in output_data folder!")
        print('Number of customers in employed data (employed.json):', len(employed_data))
        print('\n')
    else:
        print('There is an error and employed.json was not created')
        print('\n')

    if remove_ccard:
        print(f"{'remove_ccard.json'} has been created in output_data folder!")
        print('Number of customers in remove_ccard data (remove_ccard.json):', len(remove_ccard))
        print('\n')
    else:
        print('There is an error and remove_ccard.json was not created')
        print('\n')

    return customers


acw_customers = process_csv(filepath, csv_columns)
