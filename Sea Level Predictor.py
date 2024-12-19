import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = slope * years_extended + intercept
    plt.plot(years_extended, sea_levels_extended, color='red', label='Best Fit Line (1880-2050)')

    # Line of best fit (year >= 2000)
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, color='green', label='Best Fit Line (2000-2050)')

    # Customize plot
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
