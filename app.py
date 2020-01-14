# coding: UTF-8
from lib import parser
from autobuy import trader
from autobuy import calc


if __name__ == '__main__':
    args = parser.get_args()
    amount = calc.from_jpy(ticker=args.ticker, jpy=args.jpy)
    trader.buy(ticker=args.ticker, amount=amount)
