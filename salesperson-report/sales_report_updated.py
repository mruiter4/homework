def get_melons_sold_per_salesperson(sales_report_file):
    """Generate sales report showing total melons each salesperson sold."""

    salespeople = {}

    with open(sales_report_file) as f:
        for line in f:
            line.rstrip()

            salesperson, total_sales, melons_sold = line.split('|')

            #if salesperson is in the dictionary, update melons_sold; 
            #else add salesperson
            if salesperson in salespeople:
                salespeople[salesperson] += int(melons_sold)
            else:
                salespeople[salesperson] = int(melons_sold)
        return salespeople


def print_melon_sales_report(salespeople):
    """print a list of salespeople with the number of melons each sold"""

    for salesperson, melons_sold in salespeople.items():
        print(f'{salesperson} sold {melons_sold} melons')


print_melon_sales_report(get_melons_sold_per_salesperson('sales-report.txt'))