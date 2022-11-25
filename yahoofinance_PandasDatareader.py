#!/usr/bin/python3
# Vincent W
# Utilize pandas_datareader to get recent one month historical stock price from Yahoo Finance 
# $ ./yahoofinance_PandasDatareader.py AAPL

from urllib.request import DataHandler
import requests
import sys
import xlsxwriter
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import pandas_datareader as pdr
import pandas as pd
import datetime as dt
from datetime import date
from dateutil.relativedelta import relativedelta
  
import json
import argparse
from collections import OrderedDict
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) < 2:
	sys.exit("Please run script following with stock ticker to get 1 months historical price dump, for example $ ./yahoofinance_PandasDatareader.py AAPL")

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('ticker', help='')
    args = argparser.parse_args()
    ticker = args.ticker
 
    # ticker = "AAPL"
    start = date.today() - relativedelta(months=1)
    end = date.today()
 
    data = pdr.get_data_yahoo(ticker, start, end)

print(data)

df = pd.DataFrame(data)
df.to_excel(excel_writer = "ticker.xlsx")
