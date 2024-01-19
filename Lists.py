import re

def listemain():

    liste = (1,2,3,4,5,6,7,8,4,2,4)
    lmax = max(liste)
    lmin = min(liste)
    lset = set(liste)
    print(lmax, lmin, lset)

transactions =[
    {'type' : 'purchase', 'amount' : 50, 'date' : '2024-01-14'},
    {'type' : 'sale', 'amount' : 30.5, 'date' : '2024-01-15'}
]

transactions_type = transactions[0]['type']
transactions_amount = transactions[0]['amount']
transactions_date = transactions[0]['date']

def list_of(my_key):
    amount_values = [transactions['amount'] for transactions in transactions]

def sum_up(my_type):
    amount_values = [transactions['amount'] for transactions in transactions
if transactions['type'] == my_type]

def find_all(my_key,my_value):
    values = [transactions for transactions in transactions if
transactions]

def is_valid_date_format(date_string):



my_date 

listemain()