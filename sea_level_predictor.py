import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import the data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create matplotlib scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', alpha=0.6, label='Original Data')

    # 3. Create first line of best fit (using all data up to the most recent year)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate an array of years from the start year through 2050
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years_extended, intercept + slope * years_extended, 'r', label='Fit: All Data (to 2050)')

    # 4. Create second line of best fit (using data from year 2000 through the most recent year)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_val_rec, p_val_rec, std_err_rec = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate an array of years from 2000 through 2050
    years_recent_extended = pd.Series(range(2000, 2051))
    ax.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'green', label='Fit: 2000-Present (to 2050)')

    # 5. Add x-label, y-label, title, and legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save figure and return data (Do not modify this part)
    fig.savefig('sea_level_plot.png')
    return fig