# initializing string
from datetime import datetime, date

test_str = '1997'

# printing original string
print("The original string is : " + str(test_str))

# initializing format
format = "%Y"

# checking if format matches the date
res = True

# using try-except to check for truth value
try:
    res = bool(datetime.strptime(test_str, format))
except ValueError:
    res = False

# printing result
print("Does date match format? : " + str(res))
print(datetime.strptime(test_str, format))

print("2023-08-08" < "2023-07-13")

