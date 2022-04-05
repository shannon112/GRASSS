from .utils import *

def fubon_dollar_cost_averaging(
    df, money_date06, money_date16, money_date26
):
# if it's not the trading date, then postponded for 1 day.
# buy at the afternoon, not sure the actual buying point (might be close to Close)
# each time buy the stock, handling fee = 1
# options: 06, 16, 26. You're allowed to bonus 1 times.
# need to support dividends in the future (bought before X date you can get it)
    start_date = df.index[0]
    end_date = df.index[-1]

    #df_dividends = df[df['Dividends'] > 0]
    #print(df_dividends)

    df = df['Close']
    trades = []
    if money_date06 > 0:
        trades.extend(grep_monthly_valid_trade(df, start_date, end_date, 6, money_date06))
    if money_date16 > 0:
        trades.extend(grep_monthly_valid_trade(df, start_date, end_date, 16, money_date06))
    if money_date26 > 0:
        trades.extend(grep_monthly_valid_trade(df, start_date, end_date, 26, money_date06))
    return execute_trades(df, trades)