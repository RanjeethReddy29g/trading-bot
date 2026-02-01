# Binance Futures Testnet Trading Bot (Python CLI)

## Overview
This project is a Python-based command-line trading bot that interacts with the **Binance Futures Testnet (USDT-M)**.

It allows users to place **MARKET** and **LIMIT** orders using command-line arguments, with proper input validation, logging, and error handling.  
All trades are executed on **Binance Testnet**, so no real money is involved.

This project was built as part of a **Python Developer assignment**.

---

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL sides
- Command-line interface using argparse
- Input validation for all parameters
- Logs all order actions to a log file
- Graceful handling of Binance API errors

---

## Tech Stack
- Python 3.x
- python-binance
- argparse
- logging

---

## Project Structure
trading_bot/
├── cli.py
├── trading.log
├── requirements.txt
└── README.md


---

## Setup Instructions

> These steps are for anyone who downloads the project.  
> If the project already runs on your system, you do not need to repeat them.

### Step 1: Download the project
Clone the repository or download it as a ZIP file.

```bash
git clone <your-repository-url>
cd trading_bot


Step 2: (Optional) Create a virtual environment
This step is optional and recommended as a best practice.
python -m venv venv
venv\Scripts\activate   # Windows

Step 3: Install dependencies
Install required Python libraries using:
pip install -r requirements.txt


Step 4: Configure Binance Testnet API Keys
Open cli.py and add your Binance Futures Testnet API credentials:
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"
Make sure:
API keys are created on https://testnet.binancefuture.com
Futures permission is enabled
Test USDT balance is available

Usage
MARKET Order
Places a market order at the current price.
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

LIMIT Order
Places a limit order at a specified price.
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 45000

Logging
All order requests and execution messages are logged to:
trading.log
MARKET order | Symbol=BTCUSDT, Side=BUY, Qty=0.01
LIMIT order | Symbol=BTCUSDT, Side=SELL, Qty=0.01, Price=45000


Notes on Binance Testnet
Binance Futures Testnet may not always return detailed execution data such as orderId or average price.
The application handles this gracefully and confirms order placement.
This behavior is expected on testnet and does not indicate an error.

Assumptions
User has a Binance Futures Testnet account
Test USDT balance is available
API keys are valid and Futures-enabled

Author
Gouni Ranjeethreddy

Conclusion

This project demonstrates:
Python CLI development
API integration
Input validation
Logging and error handling
Real-world interaction with a trading API
