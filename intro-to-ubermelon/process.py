#open a file called um-server-01.txt and assign to a variable named log_file
log_file = open("um-server-01.txt")

#define a funtion called sales_reports that has one parameter.
def sales_reports(log_file):
    #for each line in the file
    for line in log_file:
        #strip the trailing white space
        line = line.rstrip()
        #start at the beginning of the string and assign the first 3 characters
        #to a variable named day
        day = line[0:3]
        #if the string stored in day is equal to the string "Tue", 
        #print the line
        #to update script to print sales data for Monday, change the comparison 
        #string to "Mon"
        if day == "Mon":
            print(line)

#call the sales_report function with log_file as the argument
sales_reports(log_file)
