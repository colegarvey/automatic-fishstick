
# from clients.client import *
from portfolio.acct import TradingAcct, accountSetup
from portfolio.pos import Position


def main():

    # Init Account with Alpaca data
    trade_account = accountSetup()
    if trade_account is None: 
        print("Error in account setup") 
        return

    print("bp:",trade_account.buying_power)
    print("portfolio value:",trade_account.portfolio_value)
    
    for key, val in trade_account.positions.items():
        print(f"{key}: {val.total_value}")

    # End main
    return
        


if __name__ == "__main__":
    main()