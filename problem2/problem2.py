def date_format(date_string):
    month, day, year = date_string.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
