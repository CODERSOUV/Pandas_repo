import pandas as pd

# Read the CSV file and parse the "Day" column as dates with the specified format
df = pd.read_csv('weather_data.csv', parse_dates=["Day"], date_format='%m/%d/%y')

# Now, the "Day" column should be parsed as dates with the specified format
print(df)
