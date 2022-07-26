import csv

# last_name_list = []
# # for line in sys.stdin:
# with open('employees.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('employees_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         for rows in reader:
#             mydict = {rows[6]: last_name_list.append(rows[2]) for rows in reader}
#
# print(mydict)
# -------------------------------------
import sys
from itertools import groupby

salaries_keys = []
last_names = []

# for lines in sys.stdin:
with open('employees.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        salaries_keys.append(rows[6])
        last_names.append(rows[2])

salaries_keys = dict.fromkeys(salaries_keys)

print(salaries_keys)
print(last_names)







# -------------------------------------

# DataCaptured = csv.reader('employees.csv', delimiter=',', skipinitialspace=True)
#
# salary, last_name = [], []
# for row in DataCaptured:
#     if row[6] not in salary:
#         salary.append(row[6])
#     if row[2] not in last_name:
#         last_name.append(row[2])
#
# print(salary, last_name)
# # ['Category1', 'Category2', 'Category3'] ['1994', '1995', '1996', '1998']


# ------------------------------------
# import sys
#
# employees = []
# with open('employees.csv') as f:  # data, file contains the table
#     for line in f.readlines():
#         employees.append(line.replace("\n", "").split(","))  # comma separated
#
#
# def add_values_in_dict(sample_dict, key, list_of_values):
#     """
#     append multiple values to example - file statistics key in the given dictionary
#     :param sample_dict:
#     :param key:
#     :param list_of_values:
#     :return:
#     """
#     if key not in sample_dict:
#         sample_dict[key] = list()
#     sample_dict[key].extend(list_of_values)
#     return sample_dict
#
#
# list_of_values = []
#
# for line in sys.stdin:
#     fields = line.strip().split(',')
