import twstock
import yfinance as yf
import pandas as pd
from src.mystock import MyStock, fubon_contracted_stock_ids, my_interested_stock_ids, gen_stock_name_list, test_stock_ids
from src.buy_strategy import fubon_dollar_cost_averaging
from src.sell_strategy import sell_all_at_once
import sys
import os
import argparse

# options
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--start', default=2001, help='start year')
parser.add_argument('--end', default=2021, help='end year')
parser.add_argument('--current', default=2022, help='current year')
parser.add_argument('--gaps', default=1, help='gap year ranges, min=1')
args = parser.parse_args()
stock_list = my_interested_stock_ids

# create table
table = pd.DataFrame(columns=stock_list)
table.loc[0] = gen_stock_name_list(stock_list)

# iterate through different sets
for gap in range(args.gaps):
    for year in range(args.start, args.end+1):
        # setup dates
        if year+gap+1 > args.current: continue
        mini_start_date = pd.Timestamp(year,1,6)
        vest_start_date = str(year)+'-01-01'
        vest_end_date = str(year+gap)+'-12-31'
        sell_date = str(year+gap+1)+'-01-01'

        # compute this year
        this_year_benefit = []
        for idx, stock_id in enumerate(stock_list):
            # get data
            yf_ticker = yf.Ticker(stock_id+'.TW')
            stock_history_buy = yf_ticker.history(start=vest_start_date, end=vest_end_date)
            stock_history_sell = yf_ticker.history(start=sell_date)
            this_year_benefit.append(0)

            # error handling
            if(stock_history_buy.empty or stock_history_sell.empty): 
                print('no data')
                continue
            if(stock_history_buy.index[0] > mini_start_date): 
                print('too young')
                continue

            # compute data
            bought_stock = fubon_dollar_cost_averaging(stock_history_buy, 6000, 6000, 6000)
            benefit_percentage = sell_all_at_once(stock_history_sell, bought_stock)
            this_year_benefit[-1] = benefit_percentage

        # save year row
        row_name = str(year)+'+'+str(gap+1)
        table.loc[row_name] = this_year_benefit

# output
folder_path = os.path.dirname(__file__)
output_file = os.path.splitext(os.path.basename(__file__))[0]+'.csv'
output_path = os.path.join(folder_path, 'reports', output_file)
table.to_csv(output_path)
