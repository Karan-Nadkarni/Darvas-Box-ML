import pandas as pd
import numpy as np

UPPER_BOX_LIMIT = 10
LOWER_BOX_LIMIT = -10

week_high_52 = pd.read_csv("3M_data.csv")
# number of companies currently is 15

box_check = False
stock_price = week_high_52.iloc[0]
# stock_price[0] = stock name

for i in range(1, len(stock_price) - 1):
    stock_price[i] = float(stock_price[i])
    stock_price[i + 1] = float(stock_price[i + 1])
    print(str(stock_price[i]) + "-" + str(stock_price[i + 1]) + " = " + str(stock_price[i] - stock_price[i + 1]))
    """if stock_price[i] - stock_price[i + 1] > UPPER_BOX_LIMIT:
        print("Breakout of box, buy it!!!")
    elif stock_price[i] - stock_price[i + 1] < LOWER_BOX_LIMIT:
        print("Stop loss omitted, sell it!!!")
    elif stock_price[i] - stock_price[i + 1] in range(LOWER_BOX_LIMIT, UPPER_BOX_LIMIT):
        print("Stagnating in the box")
"""