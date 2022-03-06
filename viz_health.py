import pandas as pd

# Enable the table_schema option in pandas,
# data-explorer makes this snippet available with the `dx` prefix:
pd.options.display.html.table_schema = True
pd.options.display.max_rows = None

#All countries
fullstats = './fullstatscmp.csv'
dff = pd.read_csv(fullstats)
dff

#Just 1st world western countries, no labels
firstwest = './firstwestcmpr.csv'
dfw = pd.read_csv(firstwest)
dfw
