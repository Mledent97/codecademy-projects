from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_datetime = dt.now()

#print(current_datetime)

target_year = randint(2026, 2036)

base_cost = Decimal("1000.00")
current_year = current_datetime.year

year_difference = abs(target_year - current_year)
cost_multiplier = Decimal(year_difference)
final_cost = base_cost * cost_multiplier

destinations = ['Turks', 'Barbados', 'Aruba', 'Cayman Island', 'New York']

destination = choice(destinations)

message = custom_module.generate_time_travel_message(destination, target_year, final_cost)
print(message)
