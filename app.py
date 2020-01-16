# coding: UTF-8
from lib import parser
from lib import api
from autobuy import trader
from autobuy import calc


if __name__ == '__main__':
    args = parser.get_args()
    a = api.initialize()
    amount = calc.from_jpy(api=a, ticker=args.ticker, jpy=args.jpy)
    print(trader.buy(api=a, ticker=args.ticker, amount=amount))
