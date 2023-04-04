from datetime import date, timedelta

def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)


count = 0
for d in allsundays(2022):
    count += 1

print("Number of Sunday\'s in the year 2022:", count)

if count > 0:
    student_fee = count * 800
    print("Coach will earn {} rupee\'s for the year 2022".format(student_fee))
else:
    pass
