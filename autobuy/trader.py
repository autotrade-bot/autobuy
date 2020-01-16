def buy(api, ticker, amount):
    return api.sendchildorder(product_code=ticker,
                   child_order_type="MARKET",
                   side="BUY",
                   size=amount,
                   )
