
from clients.client import *
from portfolio.acct import TradingAcct
from portfolio.pos import Position


def menu():
    print("\n#####-MENU-#####")
    print("1 - Analyze Account")
    print("2 - Analyze Symbol(s)")
    # print("3 - Run Model")
def menu2():
    print("\n#####-Analyze Symbol(s)-#####")
    print("1 - List Account Symbols")
    print("2 - Get Symbol Data")
    # print("3 - Run Model")


def main():

    # Setup user portfolio
    client = getTradingClient()
    account_data = client.get_account()
    account_assets = client.get_all_positions()

    # Setup user account
    Acct = TradingAcct(account_data)
    Acct.allocatePositions(account_assets)

    while True:
        try:
            menu()
            user_in = int(input("> "))
        except Exception as e:
            print(f"Input validation error: {e}")
            user_in = None
        
        match user_in:
            case 1:
                # do something with account
                print(Acct.buying_power)
                print(Acct.equity)
            
            case 2:
                # print another menu, 
                # start data stream with symbols ,
                symbols = [p for p in Acct.positions] 
                while True:
                    try:
                        menu2()
                        m2_in = int(input("> "))
                    except Exception as e:
                        print(f"Input validation error: {e}")
                        m2_in = None
                    
                    match m2_in:
                        case 1:
                            print(f"Positions: {symbols}")
                        case 2:
                            # get symbol data
                            sym = input("enter symbol: ")
                            elem = Acct.positions[sym]
                            elem.populateHistory()
                            print(elem.history.head(10))
                        case _:
                            break                

            # case 3:
            #     # run model on account data
            #     continue

            case _:
                break
                


    return
        


if __name__ == "__main__":
    main()