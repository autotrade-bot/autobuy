def from_jpy(api, ticker, jpy):
    ltp = api.ticker(product_code=ticker)["ltp"]
    return round(float(jpy)/ltp, 2)

