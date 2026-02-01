import argparse
import sys
import time
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# ================= LOGGING =================
logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ================= API KEYS =================
API_KEY = "vC18J3blvsaNRZ2vyeS2pkI6XHN5vnPV7X0P5ObrdmUH9HZA9AkhC9feOs6RPpCL"
API_SECRET = "WvUwE5vutNNKp0O99FyzarQ25I4MNoIe7BTLPDaYb3NMfR0zF5EG1LdD2joktSJI"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

# ================= VALIDATION =================
def validate_inputs(args):
    if args.side not in ["BUY", "SELL"]:
        print("ERROR: side must be BUY or SELL")
        sys.exit(1)

    if args.type not in ["MARKET", "LIMIT"]:
        print("ERROR: type must be MARKET or LIMIT")
        sys.exit(1)

    if args.quantity <= 0:
        print("ERROR: quantity must be greater than 0")
        sys.exit(1)

    if args.type == "LIMIT" and args.price is None:
        print("ERROR: price is required for LIMIT order")
        sys.exit(1)

# ================= MARKET ORDER =================
def place_market_order(args):
    try:
        logging.info(
            f"MARKET order | Symbol={args.symbol}, Side={args.side}, Qty={args.quantity}"
        )

        client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="MARKET",
            quantity=args.quantity
        )

        print("\nMARKET ORDER PLACED SUCCESSFULLY")
        print("Execution details may not be returned by testnet.")

        logging.info("Market order placed successfully")

    except BinanceAPIException as e:
        logging.error(f"Binance API error (MARKET): {e.message}")
        print("Binance Error:", e.message)

# ================= LIMIT ORDER =================
def place_limit_order(args):
    try:
        logging.info(
            f"LIMIT order | Symbol={args.symbol}, Side={args.side}, Qty={args.quantity}, Price={args.price}"
        )

        client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=args.quantity,
            price=args.price
        )

        print("\nLIMIT ORDER PLACED SUCCESSFULLY")
        print(f"Price: {args.price}")

        logging.info("Limit order placed successfully")

    except BinanceAPIException as e:
        logging.error(f"Binance API error (LIMIT): {e.message}")
        print("Binance Error:", e.message)

# ================= CLI =================
def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()
    validate_inputs(args)

    if args.type == "MARKET":
        place_market_order(args)
    else:
        place_limit_order(args)

if __name__ == "__main__":
    main()