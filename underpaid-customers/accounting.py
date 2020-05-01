def find_underpaid_customer_accounts(file):
  """ finds customers that owe payment"""

  melon_cost = 1.00
  #open files
  file = open(file)

  for line in file:
    #read line in file and parse input
    line = line.rstrip()
    words = line.split('|')

    fullname = words[1]
    name_parts = fullname.split()
    first_name = name_parts[0]
    last_name = name_parts[1]

    num_of_melons = float(words[2])
    #print(num_of_melons)
    amount_paid = float(words[3])

    #calculate expected payment
    expected_payment = num_of_melons * melon_cost


    #print all customer data
    print(f'{fullname} paid ${amount_paid:.2f}, expected ${expected_payment:.2f}')

    #print under and over paid accts
    if amount_paid > expected_payment:
      print(f'{first_name} overpaid for their melons')
    elif amount_paid < expected_payment:
      print(f'{first_name} underpaid for their melons')

  #close file
  file.close()
    

find_underpaid_customer_accounts("customer-orders.txt")