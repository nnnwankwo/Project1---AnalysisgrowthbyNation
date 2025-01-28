Overview 

This project analyzes GDP growth rates, population, and investment data for three countries: Nigeria, India, and the United Kingdom. The data spans from 1990 to 2028 and is sourced from an Excel file. The analysis involves filtering, calculating growth rates, and visualizing the trends for these countries.

PrerequisitesLibraries Used:
pandas: For data manipulation.
numpy: For numerical computations.
matplotlib: For creating visualizations.

Dependencies:
Python 3.x
openpyxl: For reading and writing Excel files.
Input File:The data file Countrydataproj1.xlsx must be available at the path specified in the code:
/Users/noblenwankwo/PythonCode/ECONPROJ1/Countrydataproj1.xlsxEnsure the file contains the following columns:
Country
Subject Descriptor
Year columns (e.g., 1990, 1991, ..., 2028)
Key Functionality1. Filtering Data by Countries 
The data is filtered to include only Nigeria, India, and the United Kingdom. This filtered data is saved as:
filtered_countries.xlsx
filtered_countries.csv

2. Analyzing GDP Per Capita Growth Filters data for GDP per capita (current prices).
Extracts year-by-year GDP data (1990-2028).
Calculates year-over-year growth rates.
Saves the sorted GDP growth data with average growth rates to:
gdp_growth_rate_1990_2028.xlsx

3. Visualizations

a. GDP Growth Rate for Individual CountriesPlots year-over-year GDP growth rates for Nigeria, India, and the UK.

b. Combined Graph for All CountriesDisplays a single plot comparing GDP growth rates of the three countries.

c. Period-Specific Growth Analysis (Nigeria)Analyzes average GDP growth rates for:

Pre-1991
1991–2007
2008 onward

d. Population and Investment TrendsGraphs population and total investment data for Nigeria, India, and the UK over the years.
UsageClone or download the project files.
Update the file paths in the code to match your directory structure.
Run the script in a Python environment.
OutputsGenerated Files:filtered_countries.xlsx and .csv: Filtered data for the selected countries.
gdp_growth_rate_1990_2028.xlsx: GDP growth rates and average growth rates for the selected countries.

Visualizations:Individual GDP growth rate graphs for each country.
Combined graph comparing GDP growth rates.
Population and investment trend graphs.

Key Insights This project provides insights into:
Comparative GDP growth rates for Nigeria, India, and the UK.

Period-specific growth trends for Nigeria.

Population and investment trends over the years.

 

