from pandas import *
import matplotlib.pyplot as plt

data_q2 = read_csv('C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/q2_data.csv')
data_q2['Trading Month'] = to_datetime(data_q2['Trading Month'])
data_main = data_q2[(data_q2['Markettype'] == 1) | (data_q2['Markettype'] == 4) | (data_q2['Markettype'] == 64)]
data_gem = data_q2[(data_q2['Markettype'] == 16) | (data_q2['Markettype'] == 32)]

median_pe_by_period_main = data_main.groupby('Trading Month')['P/E ratios'].median()
print(median_pe_by_period_main)
median_pe_by_period_gem = data_gem.groupby('Trading Month')['P/E ratios'].median()
plt.figure(figsize=(10, 6))
median_pe_by_period_main.plot(color='#c23531')
median_pe_by_period_gem.plot(color='#2a5caa')
plt.title('Time Series of Median P/E Ratio Over Periods')
plt.xlabel('Trading Month')
plt.ylabel('Median P/E Ratio')
plt.grid(True)
plt.legend(labels=['main board', 'gem'], loc='best')
plt.show()