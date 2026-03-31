'''
Where i peridocially test my code
'''

from utils import validate_ticker, format_currency, format_percentage

t = "AAPL"
print(validate_ticker(t))

a = "kjdsanfjksdbfjbsadljfbsdhjbf"
print(validate_ticker(a))

num = 12345678.23948
print(format_currency(num))

num = 0.565
print(format_percentage(num))