def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def next_leap(year):
    next_possible = year - (year % 4) + 4
    if is_leap(next_possible):
        return next_possible
    else:
        while is_leap(next_possible) == False:
            next_possible += 4
        return next_possible
