months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
firstDay = 2
sundays = 0

# for year in range(1900,2001):
#   if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
#     leapYear = True
#   else:
#     leapYear = False

#   for month, n in enumerate(months):
#     if firstDay == 6:
#       sundays += 1
#       firstDay = 0
#     firstDay += months[n-1] % 7

for year in range(1901, 2001):
  if (year % 4 == 0 and (not year % 100 == 0)) or (year % 100 == 0 and year % 400 == 0):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(year,"leap year")

  for month, days in enumerate(months):
    # print("month", month)
    # print("has",days, "days")
    # print("first day is", firstDay)
    if firstDay == 7:
      sundays += 1
    firstDay += days % 7
    if firstDay > 7:
      firstDay = firstDay - 7
  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  print("sun is ", sundays)
#171
#30 set apr june nov 31