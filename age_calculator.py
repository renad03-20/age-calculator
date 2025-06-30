from datetime import datetime
from dateutil.relativedelta import relativedelta

print('========= Age Calculator =========')
print('calculate your age in years months weeks hours minutes seconds in one seconds')
year = int(input('enter your year of birth YYYY: '))
months = int(input('enter your month of birth MM: '))
day = int(input('enter your day of birth DD: '))

birthdate = datetime(year, months, day)

now = datetime.now()

age = relativedelta(now, birthdate)

delta = now - birthdate
total_seconds = int(delta.total_seconds())
total_minutes = total_seconds // 60
total_hours = total_minutes // 60

print(f'\n You\'re: ')
print(f'{age.years} years')
print(f'{age.months} months')
print(f'{age.day} days')
print(f'{total_seconds} seconds')
print(f'{total_minutes} minutes')
print(f'{total_hours} hours')