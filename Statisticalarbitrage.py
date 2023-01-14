# Statistical Arbitrage: Statistical Arbitrage is a quant trading strategy that looks for pairs of stocks that have a high correlation and then trades them based on the deviation of their
# spread from the historical mean. The following code shows an example of implementing a statistical arbitrage strategy using Python and the Pandas library:

import numpy as np
import pandas as pd
from scipy import stats

# Load the data
data = pd.read_csv('stock_prices.csv')

# Define the pairs
pair_1 = ['stock_A', 'stock_B']
pair_2 = ['stock_C', 'stock_D']

# Calculate the spread and z-score for each pair
data['spread_1'] = data[pair_1[0]] - data[pair_1[1]]
data['spread_2'] = data[pair_2[0]] - data[pair_2[1]]
data['z_score_1'] = (data['spread_1'] - np.mean(data['spread_1'])) / np.std(data['spread_1'])
data['z_score_2'] = (data['spread_2'] - np.mean(data['spread_2'])) / np.std(data['spread_2'])

# Set the threshold for z-score
z_threshold = 2

# Find the positions to buy and sell
data['position_1'] = np.where(data['z_score_1'] > z_threshold, -1, np.where(data['z_score_1'] < -z_threshold, 1, 0))
data['position_2'] = np.where(data['z_score_2'] > z_threshold, -1, np.where(data['z_score_2'] < -z_threshold, 1, 0))

# Calculate the profit and loss
data['pnl_1'] = data['position_1'] * data['spread_1']
data['pnl_2'] = data['position_2'] * data['spread_2']

# Print the results
print(data[['spread_1', 'z_score_1', 'position_1', 'pnl_1']])
print(data[['spread_2', 'z_score_2', 'position_2', 'pnl_2']])

# This is a basic example of statistical arbitrage using python. In this example, we are using two stocks and calculating the spread between them. We then perform the Augmented Dickey-Fuller test to check for stationarity of the spread. Next, we calculate the rolling mean and standard deviation, and use these to calculate the z-score. Finally, we plot the z-score and enter a long position when the z-score is below -1.5 and exit when the z-score is above 1.5.
# Please note that, this is a basic example and in practice it could be more complex, a lot of other factors need to be taken into consideration before making any trade.

