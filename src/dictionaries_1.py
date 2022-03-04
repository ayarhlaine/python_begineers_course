month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print("This program will allow you to transform the short name to the long name of the month.")
print("Example: Jan to January, etc ...")
month_short_name = input("Enter any month name in short form: ")
print(month_conversions.get(month_short_name, "Not a valid month name!"))
