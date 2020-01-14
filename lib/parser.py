import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", required=True, choices=["ETH_JPY"])
    parser.add_argument("--jpy", required=True)
    args = parser.parse_args()
    return args
