import pandas as pd

#task 1
'''
df = pd.read_csv('world_population.csv')
totalPopulation = df['2022 Population'].sum()
print(("Total population: "), totalPopulation)
'''

#task 2
'''
df = pd.read_csv('world_population.csv')

if 'Country' in df.columns and '2022 Population' in df.columns and 'Area (km²)' in df.columns:

    df['2022 Population'] = pd.to_numeric(df['2022 Population'], errors='coerce')
    df['Area (km²)'] = pd.to_numeric(df['Area (km²)'], errors='coerce')

    df['Population_Density'] = df['2022 Population'] / df['Area (km²)']

    average_density = df.groupby('Country')['Population_Density'].mean().reset_index()

    average_density.rename(columns={'Population_Density': 'Average_Population_Density'}, inplace=True)

    print("\nAverage Population Density per Country:")
    print(average_density)
'''





