import os

from dotenv import load_dotenv
from solana.rpc.api import Client

import commons

load_dotenv()
ENDPOINT = os.getenv("ENDPOINT")
WALLET_ADDRESS = os.getenv("ADDRESS_0")
TOKEN = os.getenv("TOKEN")

client = Client(ENDPOINT)

token_account = commons.get_token_account(client, TOKEN, WALLET_ADDRESS)

res = client.get_token_account_balance(token_account)
print(res)
