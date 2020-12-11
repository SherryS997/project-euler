import calendar

count = 0


def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])


years = [i for i in range(1901, 2001)]
months = [j for j in range(1, 13)]
one_days = [k for k in range(1, 32)]
days = [l for l in range(1, 31)]
feb_days = [m for m in range(1, 29)]
feb_leap_years = [n for n in range(1, 30)]
o_months = [4, 6, 9, 11]
one_months = [1, 3, 5, 7, 8, 10, 12]

for x in years:
    for y in months:
        if y in one_months:
            for z in one_days:
                if findDay(str(z) + ' ' + str(y) + ' ' + str(x)) == 'Sunday' and z == 1:
                    count += 1
        elif y in o_months:
            for z in days:
                if findDay(str(z) + ' ' + str(y) + ' ' + str(x)) == 'Sunday' and z == 1:
                    count += 1
        else:
            if x == 2000:
                for z in feb_days:
                    if findDay(str(z) + ' ' + str(y) + ' ' + str(x)) == 'Sunday' and z == 1:
                        count += 1
            elif x % 4 != 0:
                for z in feb_days:
                    if findDay(str(z) + ' ' + str(y) + ' ' + str(x)) == 'Sunday' and z == 1:
                        count += 1
            else:
                for z in feb_leap_years:
                    if findDay(str(z) + ' ' + str(y) + ' ' + str(x)) == 'Sunday' and z == 1:
                        count += 1


print(count)
