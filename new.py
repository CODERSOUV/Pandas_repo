import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('csv_folder/weather_by_cities.csv')

# Group the DataFrame by 'city' column
g = df.groupby('city')

# Calculate the mean for each group
mean_by_city = g.mean()
