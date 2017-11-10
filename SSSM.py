#from time import gmtime, strftime
import math
#from datetime import *


class Trading:


# Storing stock Details
    stock_details = {
        'TEA': {'Stock_symbol': 'TEA', 'Stock_type': 'Common', 'Last_dividend': 0, 'Fixed_dividend': 'NA',
                'Par_value': 100},
        'POP': {'Stock_symbol': 'POP', 'Stock_type': 'Common', 'Last_dividend': 8, 'Fixed_dividend': 'NA',
                'Par_value': 100},
        'ALE': {'Stock_symbol': 'ALE', 'Stock_type': 'Common', 'Last_dividend': 23, 'Fixed_dividend': 'NA',
                'Par_value': 60},
        'GIN': {'Stock_symbol': 'GIN', 'Stock_type': 'Prefered', 'Last_dividend': 8, 'Fixed_dividend': 2, 'Par_value': 100},
        'JOE': {'Stock_symbol': 'JOE', 'Stock_type': 'Common', 'Last_dividend': 13, 'Fixed_dividend': 'NA',
                'Par_value': 250},
        }

        # print(stock_details)





    #Fuction to calculate dividend yield
    def calculate_dividend_yield(stock, price,stock_details):
        #curr_stock = stock
        lcl_dict = stock_details[stock]
        ld = int(lcl_dict['Last_dividend'])
        return ld / int(price)


    # print(calculate_dividend_yield('POP',20))
    #Function to calculate PE ratio
    def calculate_PE_ratio(stock,price, stock_details):
        lcl_dict = stock_details[stock]
        ld = int(lcl_dict['Last_dividend'])
        div= ld / int(price)
        return int(price) / div



    # print(calculate_PE_ratio(20,'POP'))

    #Global data struture for storing my trading records
    trading_record = []
    #Funtion to record the trade
    def record_trade(stock,init_time,trading_record):

        initial_time=init_time
        rec = []
        stock_name = stock
        #taking the inputs
        no_of_shares = input('Enter the no of shares traded: ')
        Buy_sell_indicator = input('Enter B for buy, S for sell: ')
        if Buy_sell_indicator not in ['B', 'S']:
            print('Enter the Buy Sell indicator properly')
            Buy_sell_indicator = input('Enter B for buy, S for sell')
        traded_price = input('Enter the price at which stock was traded: ')
        timestmp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        FMT="%Y-%m-%d %H:%M:%S"
        diff=(datetime.strptime(timestmp, FMT) - datetime.strptime(initial_time, FMT)).days #calculating dff bw timestamps in minutes
        diff_in_min= diff*24*60
        #only records upto t+15 mins will be stored
        if diff_in_min<=15:
            rec.extend([timestmp, stock_name, no_of_shares, Buy_sell_indicator, traded_price])
            trading_record.append(rec)
        else:
            print('Cannot record this!!!')

        print(trading_record)  #printing my trading record upto now
        #now calculating volume weighted stock price on my traded data and printing it
        trade_val = 1
        Qty = 1
        for i in trading_record:
            trade_val += (int(i[4]) * int(i[2]))
            Qty += int(i[2])
        VWSP= trade_val / Qty
        print('VMSP: ',VWSP )
        #now calculating my GM on traded data
        price = 1
        count = 0
        for i in trading_record:
            price *= int(i[4])
            count += 1
        pwr = 1 / count
        gm=math.pow(price, pwr)
        print('GM: ',gm )
        return trading_record


    # print(record_trade('TEA'))



    stock_name=input('Input the stock name: ')
    price=input('Input the price of the stock to calculate dividend yield: ')
    print('Divident yield is : ',calculate_dividend_yield(stock_name,price,stock_details))
    print('The PE ratio is : ',calculate_PE_ratio(stock_name,price,stock_details))
    choice=input('Enter 1 if you wish to record stock trading data: ')
    init_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if choice=='1':
        while True:
            stock=input('Input the stock you wanna trade, for exit press E: ')
            if stock=='E':
                break
            else:
                record_trade(stock,init_time,trading_record)
