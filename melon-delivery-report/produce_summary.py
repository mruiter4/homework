
def print_daily_melon_report(day,filename):
    the_file = open(filename)
    print(f"Day {day}: Melon Delivery Report")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print(f"Delivered {count} {melon}s for total of ${amount}")
            the_file.close()

print_daily_melon_report(1, "um-deliveries-20140519.txt")
print_daily_melon_report(2, "um-deliveries-20140520.txt")
print_daily_melon_report(3, "um-deliveries-20140521.txt")
