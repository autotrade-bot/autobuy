# coding: UTF-8
from lib import parser
from lib import api
from autobuy import trader
from autobuy import calc
from autobuy import bitbank


if __name__ == '__main__':
    args = parser.get_args()
    a = api.initialize()
    amount = calc.from_jpy(api=a, ticker=args.ticker, jpy=args.jpy)
    print(bitbank.market_buy(ticker=args.ticker, amount=amount))
