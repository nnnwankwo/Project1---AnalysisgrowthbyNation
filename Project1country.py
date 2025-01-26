#Projeect1 
import pandas as pd

# File path to the Excel file
file_path = "/Users/noblenwankwo/PythonCode/ECONPROJ1/Countrydataproj1.xlsx"

# Read in the Excel file using openpyxl
data = pd.read_excel(file_path, engine='openpyxl')

#Filter data for specific countries: India, Nigeria, UK 

countries = ["Nigeria", "India", "United Kingdom"]
filtered_countries = data[data['Country'].isin(countries)]  # Adjust 'Country' to match the actual column name

# Save filtered data for three countries to new files

filtered_countries.to_excel("/Users/noblenwankwo/PythonCode/ECONPROJ1/filtered_countries.xlsx", index=False)
filtered_countries.to_csv("/Users/noblenwankwo/PythonCode/ECONPROJ1/filtered_countries.csv", index=False)

print("Filtered data saved as 'filtered_countries.xlsx' and 'filtered_countries.csv'")

import pandas as pd
import numpy as np

# Load the data
filtered_countries = pd.read_excel('filtered_countries.xlsx')  # Ensure the file path is correct

# Filter data for specific Subject Descriptors: GDP per capita, Pop, Tot investment
subject_descriptors = [
    "Gross domestic product per capita, current prices",
    "Population",
    "Total investment"
]
filtered_subjects = filtered_countries[filtered_countries['Subject Descriptor'].isin(subject_descriptors)]

import pandas as pd
import numpy as np

# Load the filtered data (assuming the file path is provided)
df = pd.read_excel(file_path, engine='openpyxl')

# Filter data for GDP per capita (current prices) and for the specific countries (India, Nigeria, UK)
countries = ['India', 'Nigeria', 'United Kingdom']
gdp_data = df[(df['Country'].isin(countries)) & (df['Subject Descriptor'] == 'Gross domestic product per capita, current prices')]

# Extract the GDP per capita data for the years 1990 to 2028
years = [year for year in range(1990, 2029)]  # Directly use integers for the years
valid_years = [year for year in years if year in df.columns]  # Ensure these years are in the actual columns
gdp_data_years = gdp_data[valid_years]

#Verify Column names to ensure the year names are written correctly
print(df.columns.tolist())  # Display the column names to check the format


# Calculate the growth rate for each year (from 1991 onward)
gdp_growth_rate = gdp_data_years.pct_change(axis=1) * 100
gdp_growth_rate = gdp_growth_rate.replace([np.inf, -np.inf], np.nan)  # Handle any infinite values

# Add the growth rate columns to the original dataframe
df_growth = pd.concat([gdp_data[['Country']], gdp_growth_rate], axis=1)

# Calculate the average growth rate for each country
df_growth['Average Growth Rate'] = df_growth.iloc[:, 1:].mean(axis=1)

# Sort the dataframe by average growth rate in descending order
df_growth_sorted = df_growth.sort_values(by='Average Growth Rate', ascending=False)

# Save the result to a new Excel file
output_path = "/Users/noblenwankwo/PythonCode/ECONPROJ1/gdp_growth_rate_1990_2028.xlsx"
df_growth_sorted.to_excel(output_path, index=False)

# Print the location of the saved file
print(f"Sorted data saved as 'gdp_growth_rate_1990_2028.xlsx' at {output_path}")


# Print the location of the saved file
print(f"Sorted data saved as 'gdp_growth_rate_1990_2028.xlsx' at {output_path}")
 
 ######Visualization###########
###Start editing for graphs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 

 


# Load the new Excel file that contains the GDP growth rate data
file_path = "/Users/noblenwankwo/PythonCode/ECONPROJ1/gdp_growth_rate_1990_2028.xlsx"

df_growth_sorted= pd.read_excel(file_path, engine='openpyxl')


df_growth_sorted = pd.read_excel(file_path)

# Display the dataframe to verify it's loaded correctly
print(df_growth_sorted.head())

# List of countries to plot
countries = ['India', 'Nigeria', 'United Kingdom']

# Create individual graphs for each country
for country in countries:
    # Filter the data for the specific country
    country_data = df_growth_sorted[df_growth_sorted['Country'] == country]
    
    # Plot the growth rate for the country
    plt.figure(figsize=(10, 6))
    plt.plot(country_data.columns[1:-1], country_data.iloc[0, 1:-1], label=country)
    
    # Add labels and title for each country plot
    plt.title(f'GDP Growth Rate (1991-2028) for {country}')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')
    plt.legend()
    
    # Display the plot
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
