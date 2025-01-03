import os
import requests
from solders.transaction import VersionedTransaction
from solders.keypair import Keypair
from solders.commitment_config import CommitmentLevel
from solders.rpc.requests import SendVersionedTransaction
from solders.rpc.config import RpcSendTransactionConfig
from dotenv import load_dotenv
import base58
import time
import http.client
import json
from colorama import Fore, Back, Style

# Load environment variables from .env file
load_dotenv()

# Constants for the trading API
TRADING_API_URL = "https://pumpportal.fun/api/trade-local"

# Fetch wallet details from .env
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
AMOUNT = os.getenv("AMOUNT_TO_TRADE")
SLIPPAGE = os.getenv("SLIPPAGE")

if not WALLET_ADDRESS or not PRIVATE_KEY:
    raise EnvironmentError("WALLET_ADDRESS and PRIVATE_KEY must be set in the .env file.")

def executeBuySwap(contract):
    response = requests.post(url="https://pumpportal.fun/api/trade-local", data={
        "publicKey": WALLET_ADDRESS,
        "action": "buy",  # "buy" or "sell"
        "mint": contract,  # contract address of the token you want to trade
        "amount": AMOUNT,  # amount of SOL or tokens to trade
        "denominatedInSol": "true",  # "true" if amount is amount of SOL, "false" if amount is number of tokens
        "slippage": SLIPPAGE,  # percent slippage allowed
        "priorityFee": 0.005,  # amount to use as priority fee
        "pool": "pump"  # exchange to trade on. "pump" or "raydium"
    })

    keypair = Keypair.from_base58_string(PRIVATE_KEY)
    tx = VersionedTransaction(VersionedTransaction.from_bytes(response.content).message, [keypair])

    commitment = CommitmentLevel.Confirmed
    config = RpcSendTransactionConfig(preflight_commitment=commitment)
    txPayload = SendVersionedTransaction(tx, config)

    response = requests.post(
        url="https://api.mainnet-beta.solana.com/",
        headers={"Content-Type": "application/json"},
        data=SendVersionedTransaction(tx, config).to_json()
    )
    txSignature = response.json()['result']
    print(f'Transaction: https://solscan.io/tx/{txSignature}')


def executeSellSwap(contract):
    response = requests.post(url="https://pumpportal.fun/api/trade-local", data={
        "publicKey": WALLET_ADDRESS,
        "action": "sell",  # "buy" or "sell"
        "mint": contract,  # contract address of the token you want to trade
        "amount": AMOUNT,  # amount of SOL or tokens to trade
        "denominatedInSol": "true",  # "true" if amount is amount of SOL, "false" if amount is number of tokens
        "slippage": SLIPPAGE,  # percent slippage allowed
        "priorityFee": 0.005,  # amount to use as priority fee
        "pool": "pump"  # exchange to trade on. "pump" or "raydium"
    })

    keypair = Keypair.from_base58_string(PRIVATE_KEY)
    tx = VersionedTransaction(VersionedTransaction.from_bytes(response.content).message, [keypair])

    commitment = CommitmentLevel.Confirmed
    config = RpcSendTransactionConfig(preflight_commitment=commitment)
    txPayload = SendVersionedTransaction(tx, config)

    response = requests.post(
        url="https://api.mainnet-beta.solana.com/",
        headers={"Content-Type": "application/json"},
        data=SendVersionedTransaction(tx, config).to_json()
    )
    txSignature = response.json()['result']
    print(f'Transaction: https://solscan.io/tx/{txSignature}')


def getKingOfTheHill():
    conn = http.client.HTTPSConnection("pump-fun-king-of-the-hill.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "YOUR API KEY HERE",
        'x-rapidapi-host': "pump-fun-king-of-the-hill.p.rapidapi.com"
    }

    conn.request("GET", "/coins?offset=0&limit=1&sort=last_trade_timestamp&order=DESC&includeNsfw=false",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    response_json = json.loads(data.decode("utf-8"))

    # Extract the mint address
    if isinstance(response_json, list) and len(response_json) > 0 and "mint" in response_json[0]:
        mint_address = response_json[0]["mint"]
        print(f"Mint Address: {mint_address}")
    else:
        print("Mint address not found in the response.")

    return mint_address


def main():
    print("Welcome to Robert's Trading Bot!")
    try:
        print("Getting King of the hill...")
        koth = getKingOfTheHill()
        print("King of the hill found...")
        print(Fore.GREEN + "Buying KOTH...")
        executeBuySwap(koth)
        print("Waiting 30 seconds...")
        time.sleep(30)
        print(Fore.RED + "Selling KOTH...")
        executeSellSwap(koth)
        print("Waiting 10 seconds to get new KOTH...")
        time.sleep(10)
        main()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
