"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

#open the sales-report file
f = open('sales-report.txt')
#strip white space and split line on the '|' into a list called 'entries'
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    #assign the first item in entries list to salesperson
    salesperson = entries[0]
    #assign the third item in entries list to melons
    melons = int(entries[2])

    """loop over the salespeople list
        if salesperson is in the list: 
            get the index 
            use the index to update the value of melons in melons_sold
        else: 
            add salesperson and melons to respective lists"""
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#print a list of salespeople and the number of melons
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
