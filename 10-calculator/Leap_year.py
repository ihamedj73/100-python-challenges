def leap_year(year):
    if year % 4 == 0:
        if year == 100 == 0:
            if year == 400:
                return True
            return False
        return True

    return False


print(leap_year(2400))
print(leap_year(1989))
