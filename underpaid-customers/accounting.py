def find_underpaid_customer_accounts(file):
  """ finds customers that owe payment"""

  melon_cost = 1.00

  file = open(file)
  for line in file:
    line = line.rstrip()
    words = line.split('|')

    name = words[1]
    num_of_melons = float(words[2])
    amount_paid = float(words[3])
    amount_paid = format(amount_paid, '.2f')

    expected_payment = num_of_melons * melon_cost
    expected_payment = format(expected_payment, '.2f')

    if amount_paid != expected_payment:
      print(f'{name} paid ${amount_paid}, expected ${expected_payment}')
    

find_underpaid_customer_accounts("customer-orders.txt")