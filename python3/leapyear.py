# Leap Year Program by Sergio Zygmunt
# Uses the following rules to dermine if a given year is a leap year
# - Year must be evenly divisible by 4
# - Year must not be evenly divisible by 100 except if it is also divisible by 400
# - Examples: Year 2016 is a leap year. Year 700 is not a leap year since it
#   can be divided by 100 and not 400. Year 800 is a leap year despit it being
#   divisible by 100 because it is also evenly divisible by 400

year = 1600
yearStr = str(year)

if (year % 4 == 0):
        if (year % 100 != 0):
                print("Year " + yearStr + " is a leap year")
        else:
            if (year % 400 == 0):
                print("Year " + yearStr + " is a leap year since it can be evenly divided by 100 and 400.")
            else:
                print("Year " + yearStr + " isn't a leap year since it can be evenly divided by 100 but not 400.")
else:
        print("Year " + yearStr + " is not a leap year since it cannot be divided by 4")

