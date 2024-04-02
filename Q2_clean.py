from pandas import *


data_update_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_1.csv")
data_3 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/3.csv")
data_3_sub = data_3[['Stkcd', 'Markettype']]
data_q2 = data_update_1.merge(data_3_sub, left_on=['Stock Code'], right_on=['Stkcd'], how='left')
data_q2.to_csv('C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/q2_data.csv', index=False)

